from vault import Vault
from entry import Entry
from vault_manager import VaultManager
from cryptography.fernet import Fernet
import sys

key = Fernet.generate_key()
manager = VaultManager(key)
vault = Vault("User")

# Example CLI commands
vault.add_entry(Entry("Google", "user1", "password1"))
manager.save(vault, "vault.dat")
loaded = manager.load("vault.dat", "User")
print("Loaded enteries:")
for e in loaded.enteries:
    print(e.site, e.username, e.password)