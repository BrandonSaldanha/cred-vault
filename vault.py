import os
import json
from cryptography.fernet import Fernet
from entry import Entry
import requests

def validate_length(value:str, min_len: int, max_len: int, field_name: str):
    """Validate the length of a string value."""
    if not (min_len <= len(value) <= max_len):
        raise ValueError(f"{field_name} must be between {min_len} and {max_len} characters long.")

class Vault:
    def __init__(self, owner: str, key_file="encryption.key", api_url=None):
        self.owner = owner
        self.entries = []
        self.key_file = key_file
        self.api_url = api_url

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


    def upload_entry(self, site: str, username: str, password: str):
        validate_length(site, 1, 100, "Site")
        validate_length(username, 1, 50, "Username")
        validate_length(password, 1, 100, "Password")

        if not self.api_url:
            raise ValueError("API URL not set for Vault")

        encrypted_password = self.encrypt(password)

        payload = {
            "user_id": self.owner,
            "site": site,
            "username": username,
            "password": encrypted_password
        }

        response = requests.post(self.api_url, json=payload)
        if response.status_code != 200:
            raise Exception(f"Failed to upload: {response.text}")

    def fetch_entries_from_cloud(self):
        if not self.api_url:
            raise ValueError("API URL not set for Vault")

        response = requests.get(self.api_url, params={"user_id": self.owner})
        print("Raw response body:", response.text) #debug
        if response.status_code != 200:
            raise Exception(f"Failed to fetch: {response.text}")

        entries_data = response.json()
        self.entries = [
            Entry(
                site=e['site'],
                username=e['username'],
                password=self.decrypt(e['password'])
            ) for e in entries_data
        ]

    def list_entries(self):
        for entry in self.entries:
            print(f"Site: {entry.site}, Username: {entry.username}, Password: {entry.password}")