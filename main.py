import auth
import menu
import os


def main():
    while True:
        choi = int(input("1) To registration \n2) To auth \n"))
        if (choi == 1 and auth.Auth.register()):
            print("Succesfully registerd")
            clear()
        elif (choi == 2):
            menu.main(auth.Auth.login())
        else:
            print("Something went wrong")


def clear():
    sleep(5)
    os.system('clear')
    # system('cls') if u use windows


if __name__ == "__main__":
    main()
