import os
import json
from cryptography.fernet import Fernet
from entry import Entry

def validate_length(value:str, min_len: int, max_len: int, field_name: str):
    """Validate the length of a string value."""
    if not (min_len <= len(value) <= max_len):
        raise ValueError(f"{field_name} must be between {min_len} and {max_len} characters long.")

class Vault:
    def __init__(self, owner: str, key_file="encryption.key"):
        self.owner = owner
        self.entries = []
        self.key_file = key_file

        #load the encryption key from file or generate a new one if it doesn't exist
        self.encryption_key = self.load_or_generate_key()

    def load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                key = key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
        return key

    def add_entry(self, site: str, username: str, password: str):
        validate_length(site, 1, 100, "Site")
        validate_length(username, 1, 50, "Username")
        validate_length(password, 1, 100, "Password")
        entry = Entry(site, username, password)
        self.entries.append(entry)

    def list_entries(self):
        for entry in self.entries:
            print(f"Site: {entry.site}, Username: {entry.username}, Password: {entry.password}")

    def save(self, filepath: str):
        fernet = Fernet(self.encryption_key)
        data = json.dumps([e.__dict__ for e in self.entries]).encode()
        encrypted = fernet.encrypt(data)
        with open(filepath, 'wb') as f:
            f.write(encrypted)
    
    def load(self, filepath: str):
        """Load the vault from a file, decrypting the data with the stored encryption key."""
        fernet = Fernet(self.encryption_key)
        with open(filepath, 'rb') as f:
            encrypted = f.read()
        decrypted_data = fernet.decrypt(encrypted)
        entries_data = json.loads(decrypted_data.decode())
        self.entries = [Entry(**entry) for entry in entries_data] # Creates a list of Entry objects from the loaded dictionary data, unpacking each dictionary into the Entry constructor