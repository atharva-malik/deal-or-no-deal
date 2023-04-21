# Password encryption with storage
import random
import string
import json
from cryptography.fernet import Fernet
from os import listdir


passwords = {}


def initial_retrieve_password(username):
    try:
        with open(username+"storedPasses.json", "r") as f:
            # Load the contents of the file into a dictionary
            data = json.load(f)
            return data
    except Exception:
        return {}


def generate_password(length):
    # Generate a random password with the specified length
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))


def encrypt_password(password):
    # Generate a new Fernet key
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # Encrypt the password
    encrypted_password = fernet.encrypt(password.encode())

    return encrypted_password, key


def store_password(encrypted_password, key, username):
    # Store the encrypted password and key in a dictionary with the specified tag as the key
    with open("users.json", "r") as f:
        # Load the contents of the file into a dictionary
        passwords = json.loads(f.read())
    passwords[username] = (encrypted_password.decode('utf-8'), key.decode('utf-8'))
    with open("users.json", "w") as f:
        # Dump the contents of the dictionary into the file
        json.dump(passwords, f)


def delete_password(tag, username):
    try:
        del passwords[tag]
        with open(username+"storedPasses.json", "w") as f:
            # Dump the contents of the dictionary into the file
            json.dump(passwords, f)
        print("Operation successful!")
    except Exception:
        print("This password does not exist!")


def retrieve_password(tag):
    # Retrieve the encrypted password and key for the specified tag
    with open("users.json", "r") as f:
        passwords = json.loads(f.read())
    encrypted_password, key = passwords[tag]
    key = key.encode('utf-8')
    encrypted_password = encrypted_password.encode('utf-8')
    # Decrypt the password using the key
    fernet = Fernet(key)
    password = fernet.decrypt(encrypted_password).decode()

    return password


def passwords123(username):
    whatToDo = input("[R]etrieve password\n[G]enerate and store password\n[D]elete password\n[L]ist passwords\n"
                     "[E]xit\n")
    if whatToDo.lower() == "r":
        tag = input("Enter website name: ")
        try:
            retrieved_password = retrieve_password(tag)
            print(retrieved_password + "\n")
        except Exception as e:
            print("This password does not exist!")
            print("If you think this is a mistake, this is the error that occurred: " + str(e))
    elif whatToDo.lower() == "g":
        # Test the functions
        try:
            goAhead = True
            password_length = int(input("Enter password length: "))
            if password_length <= 0:
                print("Invalid length!")
                goAhead = False
            if goAhead:
                tag = input("Enter website name(will be used to retrieve passwords later): ")
                # Generate and store a new password
                try:
                    password = generate_password(password_length)
                    print("The password is: " + password)
                    encrypted_password, key = encrypt_password(password)
                    store_password(tag, encrypted_password, key, username)
                except OverflowError:
                    print("Enter a smaller length!")
        except Exception:
            print("Must be an integer!")
    elif whatToDo.lower() == "e":
        exit()
    elif whatToDo.lower() == "l":
        for i in passwords:
            retrieved_password = retrieve_password(i)
            print(str(i) + ": " + retrieved_password)
        print("\n")
    elif whatToDo.lower() == "d":
        tag = input("Enter website name: ")
        delete_password(tag, username)
    else:
        print("Wrong input please try again!\n")

try:
    with open("users.json", "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}


def add_user(username, password, secret):
    users[username] = {"password": password, "secret": secret}
    save_users()


def update_password(username, password):
    users[username]["password"] = password
    save_users()


def update_secret(username, secret):
    users[username]["secret"] = secret
    save_users()


def delete_user(username):
    del users[username]
    save_users()


def get_user_info(username):
    return users[username]


def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f)


def authenticate_user(username, password):
    if username in users and users[username]["password"] == password:
        return True
    else:
        return False


def authenticate_user_secret(username, secret):
    if username in users and users[username]["secret"] == secret:
        return True
    else:
        return False
