# Function to add tasks
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to view tasks
def view_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

# Function to mark tasks as complete
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print("Task completed:", completed_task)
    else:
        print("Invalid task index.")

# Function to remove tasks
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print("Task removed:", removed_task)
    else:
        print("Invalid task index.")

# User interface
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Remove task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        task = input("Enter the task description: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to mark as complete: "))
        complete_task(task_index)
    elif choice == "4":
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5).")