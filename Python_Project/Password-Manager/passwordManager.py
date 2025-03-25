from cryptography.fernet import Fernet
import json
import os


KEY_FILE = 'secret.key'
DATA_FILE = 'passwords.json'

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
    return Fernet(key)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def encrypt_password(fernet, password):
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(fernet, password):
    return fernet.decrypt(password.encode()).decode()

def add_password(fernet):
    site = input('Enter site name: ')
    username = input('Enter username: ')
    password = input('Enter password: ')
    encrypted_password = encrypt_password(fernet, password)

    data = load_data()
    data[site] = {'username': username, 'password': encrypted_password}
    save_data(data)
    print('Password added successfully!')

def view_passwords(fernet):
    data = load_data()
    if not data:
        print('No passwords stored.')
        return
    for site, info in data.items():
        decrypted_password = decrypt_password(fernet, info['password'])
        print(f"Site: {site}, Username: {info['username']}, Password: {decrypted_password}")

def update_password(fernet):
    data = load_data()
    site = input('Enter site name to update: ')
    if site not in data:
        print('Site not found.')
        return
    new_password = input('Enter new password: ')
    data[site]['password'] = encrypt_password(fernet, new_password)
    save_data(data)
    print('Password updated successfully!')

def delete_password():
    data = load_data()
    site = input('Enter site name to delete: ')
    if site in data:
        del data[site]
        save_data(data)
        print('Password deleted successfully!')
    else:
        print('Site not found.')

def generate_password():
    import string
    import random
    length = int(input('Enter password length: '))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f'Generated Password: {password}')

def main():
    fernet = load_key()

    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Generate Password")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_password(fernet)
        elif choice == '2':
            view_passwords(fernet)
        elif choice == '3':
            update_password(fernet)
        elif choice == '4':
            delete_password()
        elif choice == '5':
            generate_password()
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
