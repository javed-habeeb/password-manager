#this file is to creat the encryption key

#modules to import
from cryptography.fernet import Fernet

#to generate and save key
def generate_and_save_key():
    key = Fernet.generate_key()
    with open("encryption_key.key","wb") as key_file:
        key_file.write(key)
    print(f"generated key(do not disclose it!): {key.decode()}")

#inorder to use in main program.we're going to need a function that loads this key
#to load the key

def load_key():
    try:
        with open("encryption_key.key","rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("error: Encryption key not found. Run 'key_manager.py' first.")
        exit(1)

if __name__ == "__main__":
    generate_and_save_key()
