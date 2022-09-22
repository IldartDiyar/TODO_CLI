import json
import hashlib


class User:
    def __init__(self, username, name, age, hash_password):
        self.username = username
        self.name = name
        self.age = age
        self.hash_password = hash_password

    @property
    def get_username(self):
        return self.username

    @property
    def get_name(self):
        return self.name

    @classmethod
    def setter_hash_password(self, ps):
        self.hash_password = ps


class Auth:
    @classmethod
    def register(self):
        username = input("Enter username")
        name = input("Enter Name")
        age = input("Enter age")
        password = input("Enter password")
        password1 = input("Enter password to confirm")
        if (password != password1):
            print("wrong confirmation")
            registration()

        with open('user_data.json', "r+") as file_data:
            try:

                credo = {"username": username, "name": name,
                         "age": age, "password": self.hash_password(password)}
                self.write_json(credo)
                return True
            except:
                return False
            return False

    @classmethod
    def write_json(self, new_data):
        with open('user_data.json', 'r+') as file:
            file_data = json.load(file)
            file_data["Users"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)

    @classmethod
    def login(self):
        username = input("Enter username")
        password = self.hash_password(input("Enter password"))
        with open("user_data.json", "r") as file:
            file_data = json.load(file)
        for user in file_data["Users"]:
            if username == user["username"] and password == user["password"]:
                return user
            else:
                print("Wrong password or username")
                exit()

    @classmethod
    def change_password(self):
        return True

    @classmethod
    def hash_password(self, password):
        password = password.encode("utf-8")
        hashed_password = hashlib.sha256(password).hexdigest()
        return hashed_password
