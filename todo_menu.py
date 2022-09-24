import json
import os
from datetime import datetime
import time
todos = list()


def main(user_name):

    with open("todo_data.json", "r") as file_data:
        todos_data = json.load(file_data)
        for todo_data in todos_data["Todo"]:
            if todo_data.get("username") == user_name:
                todos.append(todo_data)
    os.system('clear')
    while True:
        print_list(todos)
        print('-'*25)
        choi = int(input("1)To manage ToDo\n2)Add Todo\n3)To go main menu\n"))
        print('-'*25)

        if (choi == 1):
            choi1 = int(
                input("1)To Change status\n2)To delete todo\n"))
            if (choi1 == 1 and change_status(user_name)):
                print("Status has been changed")
            if (choi1 == 2):
                print("Delete not working")
        if (choi == 2 and add_todos(user_name)):
            print("Have been added")
        if (choi == 3):
            break
        time.sleep(2)
        os.system('clear')


def print_list(todos):
    print("|id|title|date|text|status| ")
    for todo in todos:
        print(("|{0}|{1}|{2}|{3}|{4}|").format(
            todo['id'], todo['topic'], todo['date'], todo['text'], todo['status']))


def get_last_id(todos):
    last = 0
    for todo in todos:
        last = todo['id']
    return last


def add_todos(user_name):
    id = get_last_id(todos)+1
    topic = input("Write a title of todo\n")
    date = datetime.now().strftime("%d.%m.%Y")
    text = input("Write a text of todo\n")
    status = False
    with open('todo_data.json', "r+") as file_data:
        try:
            # create credo dict to insert in json file
            todo = {"id": id, "username": user_name, "topic": topic,
                    "date": date, "text": text, "status": status}
            todo_data = json.load(file_data)
            todo_data["Todo"].append(todo)
            todos.append(todo)
            # for deleting all data in json file
            file_data.seek(0)
            # inserting data to file
            json.dump(todo_data, file_data, indent=4)
            return True
        except:
            return False
        return False


def change_status(user_name):
    ids = input("Just enter id of todo\n")
    with open("todo_data.json", "r+") as file_data:

        todos_data = json.load(file_data)
        for todo in todos_data["Todo"]:
            if user_name == todo.get("username") and int(ids) == todo.get("id"):
                todo["status"] = dif(todo["status"])
                file_data.truncate(0)
                file_data.seek(0)
                json.dump(todos_data, file_data, indent=4)
                break

    for todo in todos:
        if int(ids) == todo["id"]:
            todo["status"] = dif(todo["status"])
            return True


def dif(data):
    return not data


# def delete_todo(user_name):
#     ids = input("Just enter id of todo\n")
#     with open("todo_data.json", "r+") as file_data:
#         todos_data = json.load(file_data)
#         for todo in todos_data["Todo"]:
#             if user_name == todo["username"] and int(ids) != todo["id"]:
#                 del todos_data[todo]
#                 file_data.truncate(0)
#                 file_data.seek(0)
#                 json.dump(todos_data, file_data, indent=4)
#                 break

    for todo in todos:
        if int(ids) == todo["id"]:
            todos.clear(todo)
            return True
