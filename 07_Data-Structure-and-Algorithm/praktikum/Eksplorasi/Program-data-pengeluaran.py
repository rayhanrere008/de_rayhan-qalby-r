import uuid

expenses = []

def create_expense():
    name = input("Enter expense name: ")
    amount = int(input("Enter expense amount: "))
    expense_data = {
        "id": str(uuid.uuid4()),
        "name": name,
        "amount": amount
    }
    expenses.append(expense_data)
    print("Data added !")

def view_expenses():
    total = 0
    print("All expenses")
    print("==")
    for expense in expenses:
        print(f"ID: {expense['id']}")
        print(f"Name: {expense['name']}")
        print(f"Amount: {expense['amount']}")
        print("==")
        total += expense['amount']
    print(f"== TOTAL: {total} ==")

def update_expense():
    expense_id = input("Enter expense ID: ")
    for expense in expenses:
        if expense['id'] == expense_id:
            name = input("Enter new expense name: ")
            amount = input("Enter new expense amount: ")
            if name:
                expense['name'] = name
            if amount:
                expense['amount'] = int(amount)
            print("Data updated !")
            return
    print("Expense not found.")

def delete_expense():
    expense_id = input("Enter expense ID: ")
    for expense in expenses:
        if expense['id'] == expense_id:
            expenses.remove(expense)
            print("Data deleted !")
            return
    print("Expense not found.")

def main():
    while True:
        print("\n== MENU ==")
        print("1. Create new expense data")
        print("2. View expenses")
        print("3. Update expense")
        print("4. Delete expense")
        print("5. Exit")
        print("==========")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            update_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Bye...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
