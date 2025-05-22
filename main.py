def show_menu():
    print("1. Add income")
    print("2. Add expense")
    print("3. List  transactions")
    print("4. Show balance")
    print("5. Exit")

def add_income():
    s = int(input("Enter the amount of income: "))

    if s <= 0:
        print("Please enter a positive number")
        add_income()
    else:
        print("Successfully added ",s, "to your account")

def add_expense():
    s = int(input("Enter the amount of expense: "))

    if s >= 0:
        print("Please enter a negative number")
        add_expense()
    else:
        print("Successfully taken away ",s, "to your account")