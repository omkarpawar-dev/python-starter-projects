tasks = []


def view_task():
    if len(tasks) == 0:
        print("No Task Available")
    else:
        print("These are your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_tasks():
    new_task = input("Enter your task: ")
    while True:
        confirm = input("Type 'confirm' to add the task: ").lower()
        if confirm == "confirm":
            tasks.append(new_task)
            print("Task added!")
            break
        else:
            print("You must type 'confirm' to add the task. Try again.")


def remove_task():
    if len(tasks) == 0:
        print("No tasks to remove!")
        return

    print("These are your tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    while True:
        num = input("Enter the task number to remove: ")

        if not num.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        index = int(num) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed}' removed successfully!")
            break
        else:
            print("Invalid task number! Try again.")


while True:
    print("1.View Tasks\n2. Add Tasks\n3. Remove Tasks\n4. Exit ")
    choice = input("Enter your choice: ").strip()
    if not choice.isdigit():
        print("Invalid input, Please enter a number")
    else:
        choice = int(choice)
    if choice == 1:
        view_task()
    elif choice == 2:
        add_tasks()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        break
    else:
        print("Select a valid option")
