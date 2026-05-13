# Simple Budget Tracker

budget = float(input("Enter your total budget: "))
total_spent = 0
expense_count = 0

while True:
    print("--------------------------")
    print("1 - Add an expense")
    print("2 - Check remaining budget")
    print("3 - Quit")
    print("--------------------------")

    choice = input("Choose and option: ")

    if choice == "1":
        description = input ("What did you spend money on? ")
        amount = float(input("How much did you spend? "))
        
        if amount <= 0:
            print("Amount must be greater than zero")
            continue

        total_spent = total_spent + amount
        expense_count = expense_count + 1
        remaining = budget - total_spent

        if amount >= 100:
            category = "large expense"
        elif amount <= 20:
            category = "medium expense"
        else:
            category = "small expense"

        print("Added: " + description + " - " + str(amount) + "(" + category + ")")

        if remaining <  0:
            print("WARNING: you are over budget by " + str(abs(remaining)))
        elif remaining < 50:
            print("Remaining budget: " + str(remaining))

    elif choice == "2":
        remaining = budget - total_spent
        print("Total budget: " + str(budget))
        print("Total spent: " + str(total_spent))
        print("Total expenses entered: " + str(expense_count))
        print("Remaining: " + str(remaining))

        if remaining > 0:
            print("Status: on track")
        elif remaining == 0:
            print("Status: exactly on budget")
        else:
            print("Status: over budget")

    elif choice == "3":
        print("Final summary:")
        print("Total spent: " + str(total_spent))
        print("Total expenses: " + str(expense_count))
        print("Remaining budget: " + str(budget - total_spent))
        break

    else:
        print("Invalid option — please enter 1, 2, or 3")