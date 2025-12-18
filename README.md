# Secure-Tactical-Vault 
A military-grade file encryption system using the *AES-256-CFB* algorithm.

## Overview
This project provides a secure way to encrypt sensitive documents using a password-based key derivation function (PBKDF2). It is designed for high-security environments where data integrity is paramount.

## Features
- *AES-256 Bit Encryption:* Industry standard for top-secret data.
- *Salted Key Derivation:* Uses PBKDF2 with a random 16-byte salt to prevent rainbow table attacks.
- *Integrity Protection:* Built with the cryptography backend for robust security.

## Installation

```bash
pip install -r requirements.txt
python vault.py
```

