# Personal Finance Tracker

import random
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='finance_tracker.log'
)

tips = [
    "Try cutting one non-essential expense this week",
    "Aim to save at least 20% of your income",
    "Review your subscriptions — cancel what you don't use",
    "Small daily expenses add up — track everything",
    "Build an emergency fund of 3 to 6 months of expenses"
]

options = ["Add an expense", "View summary", "Quit"]


def get_income():
    logging.debug('get_income() called')
    while True:
        income_input = input("Enter your monthly income: ")
        if income_input.lower() == "back":
            print("Nothing to go back to — please enter your income")
            logging.warning('User tried to go back at income prompt')
        else:
            try:
                income = float(income_input)
                if income <= 0:
                    print("Income must be greater than zero")
                    logging.warning('User entered invalid income: ' + str(income))
                else:
                    logging.info('Income set to: ' + str(income))
                    return income
            except ValueError:
                print("Invalid amount — please enter a number")
                logging.error('Non-numeric income entered: ' + income_input)


def print_menu():
    logging.debug('print_menu() called')
    print("----------------------------")
    for i in range(len(options)):
        print(str(i + 1) + " - " + options[i])
    print("----------------------------")


def get_description():
    logging.debug('get_description() called')
    while True:
        description = input("Enter expense description (or type 'back' to cancel): ")
        if description.lower() == "back":
            logging.info('User cancelled at description input')
            return None
        if not description:
            print("Description cannot be blank")
            logging.warning('User submitted blank description')
        else:
            logging.debug('Description entered: ' + description)
            return description


def get_amount():
    logging.debug('get_amount() called')
    while True:
        amount_input = input("Enter expense amount (or type 'back' to cancel): ")
        if amount_input.lower() == "back":
            logging.info('User cancelled at amount input')
            return None
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than zero")
                logging.warning('User entered invalid amount: ' + str(amount))
            else:
                logging.debug('Amount entered: ' + str(amount))
                return amount
        except ValueError:
            print("Invalid amount — please enter a number")
            logging.error('Non-numeric amount entered: ' + amount_input)


def get_category():
    logging.debug('get_category() called')
    while True:
        category = input("Is this essential or non-essential? (e/n or type 'back' to cancel): ")
        if category.lower() == "back":
            logging.info('User cancelled at category input')
            return None
        if category == "e" or category == "n":
            logging.debug('Category entered: ' + category)
            return category
        print("Please enter e or n")
        logging.warning('Invalid category entered: ' + category)


def add_expense(total_spent, total_essential, total_non_essential):
    logging.info('User started adding an expense')

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

    logging.info(
        'Expense saved — description: ' + description +
        ' amount: ' + str(amount) +
        ' category: ' + category +
        ' total_spent: ' + str(total_spent)
    )

    return total_spent, total_essential, total_non_essential


def view_summary(income, total_spent, total_essential, total_non_essential):
    logging.info('User viewed summary')

    assert round(total_essential + total_non_essential, 2) == round(total_spent, 2), \
        "Spending totals do not add up — essential: " + str(total_essential) + \
        " non-essential: " + str(total_non_essential) + \
        " total_spent: " + str(total_spent)

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
logging.info('Program started')

income = get_income()
total_spent = 0
total_essential = 0
total_non_essential = 0

while True:
    print_menu()
    choice = input("Choose an option: ")
    logging.debug('User selected menu option: ' + choice)

    if choice == "1":
        total_spent, total_essential, total_non_essential = add_expense(
            total_spent, total_essential, total_non_essential
        )
    elif choice == "2":
        view_summary(income, total_spent, total_essential, total_non_essential)
    elif choice == "3":
        logging.info('Program exited by user')
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid option — please enter 1, 2, or 3")
        logging.warning('Invalid menu option entered: ' + choice)