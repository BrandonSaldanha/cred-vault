# Password Manager CLI Offline

A completely offline command-line password manager that saves and loads encrypted vaults using Fernet encryption.

This version of Password Manager is complete and will live in this branch, main and other branches will become an online password manager, that you can access from multiple devices.


## Features
- Add and list password entries securely
- Vault encryption using cryptography's Fernet
- Auto-generates and stores an encryption key
- Tested with pytest

## Setup

## Easiest way
exe is located in release folder you can run from CLI :)

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
