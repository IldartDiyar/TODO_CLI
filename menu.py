import auth
import os


def main(data_user):
    print("Happy hacking")
    sleep(5)
    os.system('clear')
    user = auth.User(data_user['username'], data_user['name'],
                     data_user['age'], data_user['password'])
    while True:
        print(" — — —  MENU — — — ")
