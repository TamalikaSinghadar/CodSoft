# Define a dictionary to store tasks
tasks = {}

# Function to add a task
def add_task():
    task_name = input("Enter task name: ")
    tasks[task_name] = False

# Function to list tasks
def list_tasks():
    if tasks:
        for task, completed in tasks.items():
            status = "Done" if completed else "Not Done"
            print(f"{task} - {status}")
    else:
        print("No tasks in the list.")

# Function to mark a task as completed
def mark_completed():
    task_name = input("Enter task name to mark as completed: ")
    if task_name in tasks:
        tasks[task_name] = True
    else:
        print("Task not found!")

# Function to remove a task
def remove_task():
    task_name = input("Enter task name to remove: ")
    if task_name in tasks:
        del tasks[task_name]
    else:
        print("Task not found!")

# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
