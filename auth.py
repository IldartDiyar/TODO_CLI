import json
import hashlib


class User:
    def __init__(self, id, username, name, age, password):
        self.username = username
        self.name = name
        self.age = age
        self.password = password

    @property
    def get_username(self):
        return self.username

    @property
    def get_name(self):
        return self.name

    @property
    def get_password(self):
        return self.password

    @classmethod
    def setter_hash_password(self, ps):
        self.password = ps


class Auth:
    @classmethod
    def register(self):
        username = input("Enter username:\n")
        if (self.check_username_exist(username)):
            print("Sorry, username exist")
            self.register()
        name = input("Enter Name:\n")
        try:
            age = int(input("Enter age:\n"))
        except:
            print("Wrong input")
            self.register()
        password = input("Enter password:\n")
        password1 = input("Enter password to confirm:\n")
        if (password != password1):
            print("wrong confirmation of password")
            registration()

        with open('user_data.json', "r+") as file_data:
            try:
                credo = {"username": username, "name": name,
                         "age": age, "password": self.hash_password(password)}
                users_data = json.load(file_data)
                users_data["Users"].append(credo)
                file_data.seek(0)
                json.dump(users_data, file_data, indent=4)
                return True
            except:
                return False
            return False

    @classmethod
    def login(self):
        username = input("Enter username:\n")
        password = self.hash_password(input("Enter password:\n"))
        with open("user_data.json", "r") as file_data:
            users_data = json.load(file_data)
            for user in users_data["Users"]:
                if username == user["username"] and password == user["password"]:
                    return user
                else:
                    print("Wrong password or username")
                    exit()

    @classmethod
    def change_password(self, username):
        with open("user_data.json", "r+") as file_data:
            new_ps = input("Enter new password\n")
            users_data = json.load(file_data)
            for user in users_data["Users"]:
                if username == user["username"]:
                    user["password"] = hash_password(new_ps)
                    file_data.truncate(0)
                    file_data.seek(0)
                    json.dump(users_data, file_data, indent=4)
                    return True
                else:
                    return False

    @classmethod
    def check_new_password(self, ps, ps1):
        return self.hash_password(ps) == ps1

    @classmethod
    def check_username_exist(self, username):
        with open("user_data.json", "r") as file_data:
            users_data = json.load(file_data)
            for user in users_data["Users"]:
                if username == user["username"]:
                    return True
        return False

    @classmethod
    def hash_password(self, password):
        password = password.encode("utf-8")
        hashed_password = hashlib.sha256(password).hexdigest()
        return hashed_password
