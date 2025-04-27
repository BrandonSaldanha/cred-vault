import json
from cryptography.fernet import Fernet
from entry import Entry

class Vault:
    def __init__(self, owner: str):
        self.owner = owner
        self.entries = []

    def add_entry(self, site: str, username: str, password: str):
        entry = Entry(site, username, password)
        self.entries.append(entry)

    def list_entries(self):
        for entry in self.entries:
            print(f"Site: {entry.site}, Username: {entry.username}, Password: {entry.password}")

    def save(self, filepath: str, encryption_key: str):
        fernet = Fernet(encryption_key)
        data = json.dumps([e.__dict__ for e in self.entries]).encode()
        encrypted = fernet.encrypt(data)
        with open(filepath, 'wb') as f:
            f.write(encrypted)