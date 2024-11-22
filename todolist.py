def main():

    todo_list = []

    while True:

        operation = input("Choose an operation (view/add/remove/clear/exit): ").strip().lower()

        if operation == "view":
            view_todolist(todo_list)

        elif operation == "add":
            add_todolist(todo_list)
            print("Task added.")
        
        elif operation == "remove":
            remove_todolist(todo_list)

        elif operation == "clear":
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
            if confirm == "yes":
                todo_list.clear()
                print("All tasks cleared.")
            else:
                print("Clear operation cancelled.")

        elif operation == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid operation, please choose a valid option.")

def remove_todolist(todo):
    try:
        task_num = int(input("Enter the task number to remove: "))
        index = task_num - 1
        removed_task = todo.pop(index)
        print(f'Task "{removed_task}" removed.')
    except ValueError:
        print("Invalid input! Please enter a valid task number.")
    except IndexError:
        print("Task number is out of range.")

def add_todolist(todo):
    task = input("Enter a task: ").strip()
    if task:
        todo.append(task)
    else:
        print("Task cannot be empty. Please enter a valid task.")

def view_todolist(todo):
    if not todo:
        print("No tasks available.")
    else:
        for i, task in enumerate(todo, start=1):
            print(f"{i}. {task.title()}")

main()