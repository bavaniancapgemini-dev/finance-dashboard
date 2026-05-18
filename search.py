from database import view_transactions


def search_category(keyword):

    data = view_transactions()

    for item in data:

        if keyword.lower() in item[1].lower():

            print(item)