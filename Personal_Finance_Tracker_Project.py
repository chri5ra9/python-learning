# Personal Finance Tracker

income = float(input("Enter your monthly income: "))
total_spent = 0
total_essential = 0
total_non_essential = 0

while True:
    print("----------------------------")
    print("1 - Add an expense")
    print("2 - View summary")
    print("3 - Quit")
    print("----------------------------")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero")
            continue

        category = input("Is this essential or non-essential? (e/n): ")

        if category == "e":
            total_essential = total_essential + amount
            print("Added as essential expense: " + description)
        elif category == "n":
            total_non_essential = total_non_essential + amount
            print("Added as non-essential expense: " + description)
        else:
            print("Invalid category — expense not added")
            continue

        total_spent = total_spent + amount

    elif choice == "2":
        remaining = income - total_spent
        print("----------------------------")
        print("Monthly income:        $" + str(income))
        print("Total spent:           $" + str(total_spent))
        print("Remaining balance:     $" + str(remaining))
        print("Essential spending:    $" + str(total_essential))
        print("Non-essential spending:$" + str(total_non_essential))
        print("----------------------------")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option — please enter 1, 2, or 3")