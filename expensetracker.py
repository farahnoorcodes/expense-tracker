print("|=========EXPENSE TRACKER=========|")
print("|=================================|\n")
while True:     #continue until user chooses to exit
    print("| 1. Add Expense                  |")
    print("| 2. View Expenses                |")
    print("| 3. Calculate total spending     |")
    print("| 4. Remove Expense               |")
    print("| 5. Exit                         |")
    print("|=================================|")
    #user input for choice
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1': # if user chooses to add expense
        expense_name = input("Enter expense name: ")
        expense_amount = input("Enter expense amount: ")
        try:# Convert the amount to a float
            expense_amount = float(expense_amount)
        except ValueError:# Handle the case where the input is not a valid number
            print("Invalid amount. Please enter a valid number.")
            continue
        with open("expenses.txt", "a") as file:
            file.write(f"{expense_name}: {expense_amount}\n")
            #if user chooses to add expense, it will be added to the expenses.txt file
        print(" Expense added successfully!")
        print("|=================================|\n")
        
    elif choice == '2': #if user want to see the espense list
        print("\nYour Expenses:")
        try:
            with open("expenses.txt", "r") as file:
                expenses = file.readlines()
                if not expenses:
                    print("No expenses recorded yet.")
                else:
                    for expense in expenses:
                        print(expense.strip())
        except FileNotFoundError:
            print("No expenses recorded yet.")  
        print("|=================================|\n")
                
    elif choice == '3': #if user want to see the total spending
        total_spending = 0
        try:
            with open("expenses.txt", "r") as file:
                expenses = file.readlines()
                if not expenses:
                    print("No expenses recorded yet.")
                else:
                    for expense in expenses:
                        amount = float(expense.split(": ")[1])
                        total_spending += amount
        except FileNotFoundError:
            print("No expenses recorded yet.")
        print(f"Total spending: Rs.{total_spending:.2f}")
        print("|=================================|\n")
        
    elif choice == '4':#if user want to remove an expense
        expense_to_remove = input("Enter the expense name to remove: ")
        try:
            with open("expenses.txt", "r") as file:
                expenses = file.readlines()
        except FileNotFoundError:
            print("No expenses recorded yet.")
            continue
        with open("expenses.txt", "w") as file:
            for expense in expenses:
                if expense.split(": ")[0] != expense_to_remove:
                    file.write(expense)
        print(" Expense removed successfully!")
        print("|=================================|\n")
    elif choice == '5':#if user want to exit the program
        print("Exiting the Expense Tracker. Goodbye!")
        print("|=================================|\n")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
