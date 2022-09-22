import json
import os


def main(user_name):
    todos = list()
    with open("todo_data.json", "r+") as file_data:
        todo_data = json.load(file_data)
        for todo_data in todo_data["Todo"]:
            if user_name == todo_data["username"]:
                todos.append(todo_data)
    os.system('clear')
    while True:
        print('-'*25)
        choi = int(input("1)To modify\n2)To go main menu\n"))
        print("|id|topic|date|text|status| ")
        for todo in todos:
            print(("|{0}|{1}|{2}|{3}|{4}|").format(
                todo['id'], todo['topic'], todo['date'], todo['Text'], todo['status']))
