# Define an empty list to store expenses
expenses = []

# Function to add expenses
def add_expense(amount, category, date):
    expenses.append({"Amount": amount, "Category": category, "Date": date})
    print("Expense added.")

# Function to view expenses
def view_expenses(category=None):
    if expenses:
        if category:
            print(f"Expenses in the '{category}' category:")
            for expense in expenses:
                if expense["Category"] == category:
                    print(f"Amount: ${expense['Amount']}, Date: {expense['Date']}")
        else:
            print("All Expenses:")
            for expense in expenses:
                print(f"Amount: ${expense['Amount']}, Category: {expense['Category']}, Date: {expense['Date']}")
    else:
        print("No expenses recorded.")

# Function to calculate total spending
def calculate_total_spending():
    total = sum(expense["Amount"] for expense in expenses)
    print(f"Total spending: ${total}")

# User interface
while True:
    print("\nOptions:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total spending")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        amount = float(input("Enter the expense amount: $"))
        category = input("Enter the expense category: ")
        date = input("Enter the expense date (e.g., yyyy-mm-dd): ")
        add_expense(amount, category, date)
    elif choice == "2":
        category = input("Enter a category to filter expenses (leave empty for all): ")
        view_expenses(category)
    elif choice == "3":
        calculate_total_spending()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")