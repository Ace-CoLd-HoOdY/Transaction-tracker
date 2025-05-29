transactions = []

def show_menu():
    print()
    print("1. Add income")
    print("2. Add expense")
    print("3. List  transactions")
    print("4. Show balance")
    print("5. Exit")
    print()

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

def show_balance():
    if len(transactions) == 0:
        total = 0
    else:
        total = sum(transactions)
    
    print(f"Your balance: {total}")

while True:
    show_menu()
    choice = int(input("Choose what you want: "))
    if choice == 1:
        print()
        add_income()
        print()
    elif choice == 2:
        print()
        add_expense()
        print()
    elif choice == 3:
        print()
        list_transactions()
        print()
    elif choice == 4:
        print()
        show_balance()
        print()
    elif choice == 5:
        print()
        print("Get out!")
        break
    else:
        print()
        print("Wrong choice")
        print()