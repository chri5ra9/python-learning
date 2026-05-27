# Personal Finance Tracker

import random
import sys

tips = [
    "Try cutting one non-essential expense this week",
    "Aim to save at least 20% of your income",
    "Review your subscriptions — cancel what you don't use",
    "Small daily expenses add up — track everything",
    "Build an emergency fund of 3 to 6 months of expenses"
]

options = ["Add an expense", "View summary", "Quit"]


def get_income():
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
                    return income
            except ValueError:
                print("Invalid amount — please enter a number")


def print_menu():
    print("----------------------------")
    for i in range(len(options)):
        print(str(i + 1) + " - " + options[i])
    print("----------------------------")


def get_description():
    while True:
        description = input("Enter expense description (or type 'back' to cancel): ")
        if description.lower() == "back":
            return None
        if not description:
            print("Description cannot be blank")
        else:
            return description


def get_amount():
    while True:
        amount_input = input("Enter expense amount (or type 'back' to cancel): ")
        if amount_input.lower() == "back":
            return None
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than zero")
            else:
                return amount
        except ValueError:
            print("Invalid amount — please enter a number")


def get_category():
    while True:
        category = input("Is this essential or non-essential? (e/n or type 'back' to cancel): ")
        if category.lower() == "back":
            return None
        if category == "e" or category == "n":
            return category
        print("Please enter e or n")


def add_expense(total_spent, total_essential, total_non_essential):
    description = get_description()
    if description is None:
        print("Expense cancelled — returning to menu")
        return total_spent, total_essential, total_non_essential

    amount = get_amount()
    if amount is None:
        print("Expense cancelled — returning to menu")
        return total_spent, total_essential, total_non_essential

    category = get_category()
    if category is None:
        print("Expense cancelled — returning to menu")
        return total_spent, total_essential, total_non_essential

    if category == "e":
        total_essential = total_essential + amount
        print("Added as essential expense: " + description)
    elif category == "n":
        total_non_essential = total_non_essential + amount
        print("Added as non-essential expense: " + description)

    total_spent = total_spent + amount
    return total_spent, total_essential, total_non_essential


def view_summary(income, total_spent, total_essential, total_non_essential):
    remaining = income - total_spent
    print("----------------------------")
    print("Monthly income:         $" + str(income))
    print("Total spent:            $" + str(total_spent))
    print("Remaining balance:      $" + str(remaining))
    print("Essential spending:     $" + str(total_essential))
    print("Non-essential spending: $" + str(total_non_essential))
    print("----------------------------")
    print("Tip: " + random.choice(tips))


# main program
income = get_income()
total_spent = 0
total_essential = 0
total_non_essential = 0

while True:
    print_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        total_spent, total_essential, total_non_essential = add_expense(
            total_spent, total_essential, total_non_essential
        )
    elif choice == "2":
        view_summary(income, total_spent, total_essential, total_non_essential)
    elif choice == "3":
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid option — please enter 1, 2, or 3")