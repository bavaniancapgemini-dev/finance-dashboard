from database import view_transactions


def total_income():

    data = view_transactions()

    total = 0

    for item in data:

        if item[0] == "income":

            total += item[2]

    return total



def total_expense():

    data = view_transactions()

    total = 0

    for item in data:

        if item[0] == "expense":

            total += item[2]

    return total