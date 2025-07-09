# 🔐 Password Manager CLI

This is a beginner-friendly command-line password manager built with Python.

## 🚀 What It Does

- Generates random passwords (numbers, letters, or both)
- Lets you save them under names like "gmail" or "instagram"
- Encrypts passwords so they're unreadable outside the program
- Saves your data to a file (`.json`) so it's not lost
- Can read the saved file and decrypt passwords only if you run the program

## 📁 Files Explained

- `key_manager.py`: Creates the encryption key
- `passwordgenerator.py`: The main app (menu, generate, save, load, etc.)

## 🛠️ How to Use

1. First, create the encryption key:
   in bash: "python3 key_manager.py" 
   what it does ----> creates an 'encrypted_key.key' file 

2. Second, run the main program
   in bash: "python3 key_manager.py"
