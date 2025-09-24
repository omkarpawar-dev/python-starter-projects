expenses = []

def add_exp():
    try:
        amount = int(input("Enter the amount:"))
        category = input("Enter the category[ One Word ]: ").strip()
        while not category.isalpha():
            print("Invalid Category, Enter Letters Only")
            category = input("Enter the category[ One Word ]: ").strip()
        date = input("Enter date in DD-MM-YY format: ")
        desc = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "date": date,
            "desc": desc
        }

        expenses.append(expense)

        with open("expense.txt", "a") as f:
            f.write(f"{amount} | {category} | {date} | {desc}\n")
            print("Expense added successfully!")
    except ValueError:
        print("Invalid input amount must be a number.")


def view_exp():
    try:
        with open("expense.txt") as f:
            lines = f.readlines()
            if len(lines) == 0:
                print("No Tasks Added!")
                return
            print("Sr no.| Amount | Category | Date | Description")
            print(
                "__________________________________________________________________________")
            for i, line in enumerate(lines, start=1):
                print(i, line.strip())
    except FileNotFoundError:
        print("File not Found!")


def del_exp():
    try:
        with open("expense.txt") as f:
            lines = f.readlines()
            if len(lines) == 0:
                print("No expenses to delete!")
                return
            print("Sr no.| Amount | Category | Date | Description")
            print(
                "__________________________________________________________________________")
            for i, line in enumerate(lines, start=1):
                print(i, line.strip())

        try:
            num = int(input("Enter the Sr no. you want to delete: "))
        except ValueError:
            print("Enter a valid Sr no.")
            return

        if num < 1 or num > len(lines):
            print("Type a valid sr no.")
            return

        del_line = lines.pop(num - 1)

        with open("expense.txt", "w") as f:
            f.writelines(lines)

        if len(expenses) >= num:
            expenses.pop(num - 1)

        print("Deleted expense:", del_line.strip())
        print("Expense deleted successfully!")

    except FileNotFoundError:
        print("Expenses file not found!")


while True:
    print("1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Exit")
    user_input = (input("Enter your choice: "))
    if not (user_input).isdigit():
        print("Please Enter a valid Number")
        continue
    choice = int(user_input)
    if (choice) > 4 or choice < 1:
        print("Enter a valid choice number")
    elif (choice) == 1:
        add_exp()
    elif (choice) == 2:
        view_exp()
    elif (choice) == 3:
        del_exp()
    else:
        break
