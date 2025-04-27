import json
from cryptography.fernet import Fernet
from vault import Vault
from entry import Entry

class VaultManager:
    def __init__(self, key: bytes):
        self.fernet = Fernet(key)
    
    def save(self, vault: Vault, filepath: str):
        data = json.dumps([e.__dict__ for e in vault.entries]).encode()
        encrypted = self.fernet.encrypt(data)
        with open(filepath, 'wb') as file:
            file.write(encrypted)
    
    def load(self, filepath: str, owner: str) -> Vault:
        with open(filepath, 'rb') as file:
            encrypted = file.read()
        decrypted = self.fernet.decrypt(encrypted)
        entries_data = json.loads(decrypted.decode())
        vault = Vault(owner)
        for e in entries_data:
            vault.add_entry(Entry(**e))
        return vault

