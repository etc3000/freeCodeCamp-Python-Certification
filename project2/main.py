'''
Program Summary
---------------
This program implements a budgeting system using a Category class and a
spending chart generator.

Components
----------
1. Category Class
   Represents a budget category (e.g., Food, Clothing, Entertainment).

   Attributes:
   - name: Category name.
   - ledger: List of transactions, each containing an amount and description.
   - budget: Running balance for the category.

   Methods:
   - deposit(amount, description=""):
       Adds funds to the category and records the transaction.

   - withdraw(amount, description=""):
       Removes funds if sufficient funds exist and records the transaction.

   - transfer(amount, category):
       Transfers funds between categories and records the transactions.

   - get_balance():
       Returns the current category balance.

   - check_funds(amount):
       Verifies sufficient funds are available.

   - __str__():
       Produces a formatted ledger display including transactions and balance.

2. create_spend_chart(categories)
   Generates a text-based bar chart illustrating spending percentages
   by category.

   Functionality:
   - Calculates total withdrawals for each category.
   - Converts spending into percentage values rounded down to the nearest 10%.
   - Builds a vertical percentage chart using 'o' markers.
   - Displays category names vertically beneath the chart.

Purpose
-------
The program provides simple budget tracking with support for deposits,
withdrawals, transfers, balance checking, transaction history, and
visual spending analysis across multiple budget categories.
'''

import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.budget = 0

    def __str__(self):
        display = (
            "*" * int((30 - len(self.name)) / 2)
            + self.name
            + "*" * int((31 - len(self.name)) / 2)
            + "\n"
        )

        for operation in self.ledger:
            amount = f"{operation['amount']:.2f}"
            description = operation["description"][:23]
            spaces = 30 - len(description) - len(amount)
            display += f"{description}{' ' * spaces}{amount}\n"

        display += f"Total: {self.budget:.2f}"
        return display

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def deposit(self, amount, description=""):
        self.budget += amount
        self.ledger.append(
            {
                "amount": amount,
                "description": description,
            }
        )

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.budget -= amount
            self.ledger.append(
                {
                    "amount": -amount,
                    "description": description,
                }
            )
            return True

        return False

    def get_balance(self):
        return self.budget

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

        return False


def create_spend_chart(categories):
    category_names = [category.name for category in categories]

    category_withdrawals = []
    for category in categories:
        total = sum(
            operation["amount"]
            for operation in category.ledger
            if operation["amount"] < 0
        )
        category_withdrawals.append(abs(total))

    total_withdrawals = sum(category_withdrawals)

    category_withdrawals = [
        math.floor(((withdrawal / total_withdrawals) * 100) / 10) * 10
        for withdrawal in category_withdrawals
    ]

    chart = "Percentage spent by category\n"

    spaces = [" " for _ in range(3 * len(categories) - 1)]

    for percentage in range(100, -1, -10):
        chart += f"{' ' * (3 - len(str(percentage)))}{percentage}|"

        for index, withdrawal in enumerate(category_withdrawals):
            if withdrawal == percentage:
                spaces[index * 3 + 1] = "o"

        chart += "".join(spaces) + "  \n"

    divider = ["-" for _ in range(len(spaces) + 2)]
    chart += " " * 4 + "".join(divider) + "\n"

    max_length = max(len(name) for name in category_names)

    for i in range(max_length):
        chart += " " * 5

        for j, name in enumerate(category_names):
            chart += name[i] if len(name) > i else " "

            if j == len(category_names) - 1:
                if i == max_length - 1:
                    chart += "  "
                    return chart
                chart += "  \n"
            else:
                chart += "  "
