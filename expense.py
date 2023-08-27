import time
from prettytable import PrettyTable
import re


def display_menu():
    print()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("%  [A] = Add an expense    %")
    print("%  [B] = Generate a report %")
    print("%  [C] = Exit              %")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print()


def main(expenses):
    print()
    print("╔═══════════════════════════════════════════╗")
    print("║      WELCOME TO YOUR EXPENSE TRACKER      ║")
    print("╚═══════════════════════════════════════════╝")

    menu_options = ("A", "B", "C")

    while True:
        display_menu()

        user_input = get_user_input(menu_options)

        if user_input in menu_options:
            break
        else:
            print("OPTION NOT AVAILABLE")

    if user_input == "A":
        Add_expense(expenses, expense_categories)
    elif user_input == "B":
        generate_report(expenses)
    elif user_input == "C":
        print("Exiting...")
        time.sleep(1)
        return


def get_user_input(menu_options):
    while True:
        user_input = input("Enter an option: ").upper()

        if user_input in menu_options:
            return user_input
        else:
            print("OPTION NOT AVAILABLE")


def get_expense_category(categories):
    print("Available Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category} {get_category_emoji(category)}")

    while True:
        try:
            category_choice = input(
                "Select a Category from the list (by number) or type 'exit': "
            )

            if category_choice == "exit":
                print("Cancelling category selection.")
                break

            category_choice = int(category_choice)

            if 1 <= category_choice <= len(categories):
                expense_category = categories[category_choice - 1]
                return expense_category
            else:
                print("Invalid choice. Please select a valid category or type 'exit'.")
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit'.")


def Add_expense(expenses, categories):
    while True:
        amount = input("Enter an amount in $ (or type 'exit' to exit the program): ")

        if amount.lower() == "exit":
            break

        if "$" in amount:
            amount_str = amount.replace("$", "")
        else:
            amount_str = amount

        amount = validate_amount_input(amount_str)
        if amount is None:
            continue

        print()

        while True:
            date = input("Enter a date of the expense (YYYY/MM/DD): ")

            if re.match(r"^\d{4}/\d{2}/\d{2}$", date):
                print("Valid date format.")
                break
            else:
                print("Invalid date format. Please use YYYY/MM/DD format.")

        print()

        expense_category = get_expense_category(categories)

        expense = {
            "amount": f"{amount}$",
            "date": date,
            "expense category": expense_category,
        }
        expenses.append(expense)

        print()

        table = PrettyTable(["Amount", "Date", "Expense Category"])
        for exp in expenses:
            table.add_row([exp["amount"], exp["date"], exp["expense category"]])

        print("Expense added successfully")
        print(table)


def validate_amount_input(input_str):
    if input_str.lower() == "exit":
        return None

    if "$" in input_str:
        amount_str = input_str.replace("$", "")
    else:
        amount_str = input_str

    try:
        amount = float(amount_str)
        print("Amount:", amount, "$")
        return amount
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return None


def generate_report(expenses):
    table = PrettyTable(["Amount", "Date", "Expense Category"])
    for exp in expenses:
        table.add_row([exp["amount"], exp["date"], exp["expense category"]])

    print("Expense Report:")
    print(table)


def get_category_emoji(category):
    emoji_map = {"Food": "🍔", "Home": "🏠", "Work": "💼", "Fun": "🎉", "Misc": "📦"}
    return emoji_map.get(category, "")


expense_categories = ["Food 🍔", "Home 🏠", "Work 💼", "Fun 🎉", "Misc 📦"]

expenses_list = []
if __name__ == "__main__":
    main(expenses_list)