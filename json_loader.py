import json
import getpass
import hashlib


human_data_file = "human_info.json"

signed = False


def hash_i(password):
    return hashlib.sha256(password.encode()).hexdigest()

#? Storing data
def store_data(username, password):
    new_data = {
        "name": username,
        "password": hash_i(password)
    }

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

    password = getpass.getpass("Enter new password: ")

    store_data(name, password)

    print("Username and Password stored")

else:
    data = load_data()

    if data:
        print(data["name"], "is registered. Please enter password for it.")

        check_password = getpass.getpass("Enter password: ")

        if hash_i(check_password) == data["password"]:
            print("Password correct!\nSuccessfully signed in.")

            signed = True

        else:
            print("Incorrect password!")

    else:
        print("No User is registered!")

