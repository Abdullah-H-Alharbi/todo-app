import functions
from functions import get_todos
import time
now = time.strftime("%Y-%m-%d %H:%M:%S")
print("it is :", now)
#from functions import get_todos , write_todos
while True:
    user_action = input("type add,show, complete , edit , exit : ")
    user_action = user_action.strip()

#to check
    if user_action.startswith('add') :
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)
    elif user_action.startswith('show') :

        todos = functions.get_todos()

        for index , ite in enumerate (todos):
            ite = ite.strip('\n')
            raw = f"[{index + 1}]-{ite}"
            print(raw)
    elif user_action.startswith('edit'):
        try :
            Number = int(user_action[5:])
            Number = Number - 1

            todos = functions.get_todos()

            new_task = input("enter new task : ")
            todos[Number] = new_task + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("your command is not valid ")
            continue

    elif user_action.startswith('complete') :
        try :
            number = int(user_action[9:])
            todos = get_todos('todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)

            message = f" to do {todo_to_remove} was removed from the list."
            print(message)
        except IndexError :
            print("There is no item with that number")
            continue
    elif user_action.startswith('exit') :
        break

    else :
        print("invalid input")


