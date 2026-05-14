# Personal Finance Tracker

import random
import sys

while True:
    income_input = input("Enter your monthly income: ")
    if income_input.lower() == "back":
        print("Nothing to go back to — please enter your income")
    else:
        try:
            income = float(income_input)
            if income <= 0:
                print("Income must be greater than zero")
            else:
                break
        except ValueError:
            print("Invalid amount — please enter a number")

total_spent = 0
total_essential = 0
total_non_essential = 0

tips = [
    "Try cutting one non-essential expense this week",
    "Aim to save at least 20% of your income",
    "Review your subscriptions — cancel what you don't use",
    "Small daily expenses add up — track everything",
    "Build an emergency fund of 3 to 6 months of expenses"
]

options = ["Add an expense", "View summary", "Quit"]

while True:
    print("----------------------------")
    for i in range(len(options)):
        print(str(i + 1) + " - " + options[i])
    print("----------------------------")

    choice = input("Choose an option: ")

    if choice == "1":
        cancelled = False

        # description input
        while True:
            description = input("Enter expense description (or type 'back' to cancel): ")
            if description.lower() == "back":
                cancelled = True
                break
            if not description:
                print("Description cannot be blank")
            else:
                break

        if cancelled:
            print("Expense cancelled — returning to menu")
            continue

        # amount input
        while True:
            amount_input = input("Enter expense amount (or type 'back' to cancel): ")
            if amount_input.lower() == "back":
                cancelled = True
                break
            try:
                amount = float(amount_input)
                if amount <= 0:
                    print("Amount must be greater than zero")
                else:
                    break
            except ValueError:
                print("Invalid amount — please enter a number")

        if cancelled:
            print("Expense cancelled — returning to menu")
            continue

        # category input
        while True:
            category = input("Is this essential or non-essential? (e/n or type 'back' to cancel): ")
            if category.lower() == "back":
                cancelled = True
                break
            if category == "e" or category == "n":
                break
            print("Please enter e or n")

        if cancelled:
            print("Expense cancelled — returning to menu")
            continue

        # save the expense
        if category == "e":
            total_essential = total_essential + amount
            print("Added as essential expense: " + description)
        elif category == "n":
            total_non_essential = total_non_essential + amount
            print("Added as non-essential expense: " + description)

        total_spent = total_spent + amount

    elif choice == "2":
        remaining = income - total_spent
        print("----------------------------")
        print("Monthly income:         $" + str(income))
        print("Total spent:            $" + str(total_spent))
        print("Remaining balance:      $" + str(remaining))
        print("Essential spending:     $" + str(total_essential))
        print("Non-essential spending: $" + str(total_non_essential))
        print("----------------------------")
        print("Tip: " + random.choice(tips))

    elif choice == "3":
        print("Goodbye!")
        sys.exit()

    else:
        print("Invalid option — please enter 1, 2, or 3")