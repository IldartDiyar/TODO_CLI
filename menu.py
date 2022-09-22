import auth
import os

from time import sleep


class TodoList:
    def __init__(self, id, username, topic, date, text, finished):
        self.id = id
        self.username = username
        self.topic = topic
        self.date = date
        self.text = text
        self.finished = finished


def main(data_user):
    print("Happy hacking")
    sleep(1)
    os.system('clear')
    user = auth.User(data_user['username'], data_user['name'],
                     data_user['age'], data_user['password'])
    while True:
        print(" Hello,", user.get_name)
        print("1) To working with TODO list")
        print("2) To change password")
        print("3) Exit ")
        choi = int(input())
        if choi == 1:

        if choi == 2:
            ps1 = user.get_password
            ps = input("Enter u current password\n")
            if (auth.Auth.check_new_password(ps, ps1) and auth.Auth.change_password(user.get_username)):
                print("Password Changed")
            else:
                print("sorry, ur password wrong")
        if choi == 3:
            exit()
