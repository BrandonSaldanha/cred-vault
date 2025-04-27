# password-manager
This is a Python CLI password manager
# Password Manager CLI

A command-line password that saves and loads encrypted vaults using Fernet encryption.

## Features
- Add and list password entries securely
- Vault encryption using cryptography's Fernet
- Auto-generates and stores an encryption key
- Tested with pytest

## Setup

### On Linux/macOS:
```bash
chmod +x setup.sh
./setup.sh
```

### On Windows (PowerShell):
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
./setup.ps1
```

## Run Tests
```bash
pytest
