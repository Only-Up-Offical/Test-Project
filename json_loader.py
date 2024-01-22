import json
import getpass
import hashlib


human_data_file = "human_info.json"

signed = False


def hash_i(password):
    return hashlib.sha256(password.encode()).hexdigest()

#? Storing data
def store_data(username, password):
    
    try:

        with open(human_data_file, 'r') as file:
            new_data = json.load(file)
    except:
        new_data = {}

    new_data[username] = hash_i(password)

    with open(human_data_file, 'w') as file:
        json.dump(new_data, file)

#? Loading user data
def load_data():
    try:
        with open(human_data_file, 'r') as file:
            return json.load(file)
    except:
        return None

option = input("Are you new here (y/n): ")

if option == 'y':
    name = input("Enter new username: ")

    password = getpass.getpass(prompt="Enter new password: ")

    store_data(name, password)

    print("Username and Password stored")

else:
    data = load_data()

    if data:
        check_name = input("Enter username: ")

        check_password = getpass.getpass(prompt="Enter password: ")

        if hash_i(check_password) == data[check_name]:
            print("Password correct!\nSuccessfully signed in.")

            signed = True

        else:
            print("Incorrect password!")

    else:
        print("No users are registered!")

