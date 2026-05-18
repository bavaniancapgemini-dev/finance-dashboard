from database import (
    add_transaction,
    view_transactions,
    delete_transaction
)

from reports import (
    total_income,
    total_expense
)

from search import search_category

from utils import title


while True:

    title()

    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Search Category")
    print("4. Delete Transaction")
    print("5. Income Report")
    print("6. Expense Report")
    print("7. Exit")

    choice = input("Choose: ")


    if choice == "1":

        transaction_type = input(
            "Type (income/expense): "
        )

        category = input("Category: ")

        amount = int(input("Amount: "))

        add_transaction(
            transaction_type,
            category,
            amount
        )

        print("Transaction Added")


    elif choice == "2":

        data = view_transactions()

        for item in data:

            print(item)


    elif choice == "3":

        keyword = input("Search category: ")

        search_category(keyword)


    elif choice == "4":

        category = input(
            "Category to delete: "
        )

        delete_transaction(category)

        print("Transaction Deleted")


    elif choice == "5":

        print(
            "Total Income:",
            total_income()
        )


    elif choice == "6":

        print(
            "Total Expense:",
            total_expense()
        )


    elif choice == "7":

        break


    else:

        print("Invalid Choice")