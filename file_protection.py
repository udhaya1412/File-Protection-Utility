from cryptography.fernet import Fernet

# Generate key
def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt file
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")

# Decrypt file
def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open("decrypted_" + filename.replace(".encrypted", ""), "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")

# Main menu
print("1. Generate Key")
print("2. Encrypt File")
print("3. Decrypt File")

choice = input("Enter choice: ")

if choice == "1":
    generate_key()

elif choice == "2":
    file_name = input("Enter file name to encrypt: ")
    encrypt_file(file_name)

elif choice == "3":
    file_name = input("Enter encrypted file name: ")
    decrypt_file(file_name)

else:
    print("Invalid choice")