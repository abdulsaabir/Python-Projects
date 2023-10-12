# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    for existing_task in tasks:
        if existing_task["task"] == task:
            print("Task already exists. Cannot add duplicate task.")
            return
    tasks.append({"task": task, "done": False})
    print('Task added successfully')

# Function to edit a task
def edit_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task
        print('Task edited successfully')

# Function to mark a task as done
def mark_task_as_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f'Task "{tasks[index]["task"]}" is Done ✅')

# Function to delete a task
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print('Task deleted successfully')

# Function to display the task list
def display_tasks():
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i+1}. {task['task']} - Status: {status}")

# Function to check if a string contains alphabetic characters
def has_alpha(text):
    return any(char.isalpha() for char in text)

while True:
    # User menu
    print("\nOptions: add, edit, delete, done, list, quit")
    
    # Get user input
    user_input = input(": ")
    
    # Check for user choice
    if user_input == "quit":
        break
    elif user_input == "add":
        task = input("Enter the task: ")
        if has_alpha(task):
            add_task(task)
        else:
            print("Invalid input. Task name must contain alphabetic characters.")
    elif user_input == "edit":
        display_tasks()  # Print the list of tasks before editing
        try:
            index = int(input("Enter the task number to edit: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter the new task: ")
                if has_alpha(new_task):
                    edit_task(index, new_task)
                else:
                    print("Invalid input. New task name must contain alphabetic characters.")
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Task number must be a valid number.")
    elif user_input == "delete":
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                delete_task(index)
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Task number must be a valid number.")
    elif user_input == "done":
        display_tasks()
        try:
            index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                mark_task_as_done(index)
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Task number must be a valid number.")
    elif user_input == "list":
        display_tasks()
    else:
        print("Invalid input")
