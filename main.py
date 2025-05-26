transactions = []

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
        transactions.append(s)

def add_expense():
    s = int(input("Enter the amount of expense: "))

    if s >= 0:
        print("Please enter a negative number")
        add_expense()
    else:
        print("Successfully taken away ",s, "to your account")
        transactions.append(s)

def list_transactions():
    if len(transactions) == 0:
        print("No trasactions")
    else:
        for i in transactions:
            if i < 0:
                print("Expense", i)
            else:
                print("Income", i)



show_menu()
choice = int(input("Choose what you want: "))

while True:
    if choice == 1:
        add_income()
    elif choice == 2:
        add_expense()
    elif choice == 3:
        list_transactions()
    elif choice == 4:
        print("not now")
    elif choice == 5:
        print("Get out!")
        break