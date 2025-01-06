from cryptography.fernet import Fernet

# Function to generate and write a key (used initially to create the key file)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)  # Save the key to a file

# Function to load the key from the key file
def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# Ensure the key file exists before running the program
try:
    key = load_key()
except FileNotFoundError:
    print("Key file not found. Generating a new key...")
    write_key()
    key = load_key()

# Prompt for master password
master_pwd = input("What is the master password? ").encode()
fer = Fernet(key)

# Function to view saved passwords
def view():
    try:
        with open("passwords.txt", "r") as f:  # Open file in read mode
            for line in f.readlines():
                data = line.rstrip()  # Remove trailing newline characters
                user, encrypted_passw = data.split("|")
                decrypted_passw = fer.decrypt(encrypted_passw.encode()).decode()
                print(f"User: {user}, Password: {decrypted_passw}")
    except FileNotFoundError:
        print("No passwords file found. Add some passwords first!")

# Function to add new passwords
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()  # Encrypt and convert to string
    with open("passwords.txt", "a") as f:  # Append mode
        f.write(name + "|" + encrypted_pwd + "\n")
    print("Password added successfully!")

# Main program loop
while True:
    mode = input("Would you like to add a new password or view an existing one (view/add)? Press q to quit: ").lower()
    if mode == "q":
        print("Goodbye!")
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")


