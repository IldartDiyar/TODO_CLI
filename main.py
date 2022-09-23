import auth
import menu
import os
from time import sleep


def main():
    while True:
        # here first menu
        choi = int(input("1) To registration \n2) To auth \n3) To exit\n"))
        if (choi == 1 and auth.Auth.register()):
            print("Succesfully registerd")
            # just for clearing comand line
            clear()
        elif (choi == 2):
            # here going to auth if auth happen
            menu.main(auth.Auth.login())
        elif (choi == 3):
            exit()
        else:
            print("Something went wrong")


def clear():
    sleep(1)
    os.system('clear')
    # system('cls') if u use windows


if __name__ == "__main__":
    # program starts here
    main()
