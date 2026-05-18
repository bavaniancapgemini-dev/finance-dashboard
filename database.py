import sqlite3


connection = sqlite3.connect("finance.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (

    type TEXT,
    category TEXT,
    amount INTEGER

)
""")

connection.commit()

connection.close()

def add_transaction(transaction_type, category, amount):

    connection = sqlite3.connect("finance.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO transactions VALUES (?, ?, ?)",
        (transaction_type, category, amount)
    )

    connection.commit()

    connection.close()

def view_transactions():

    connection = sqlite3.connect("finance.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM transactions")

    data = cursor.fetchall()

    connection.close()

    return data

def delete_transaction(category):

    connection = sqlite3.connect("finance.db")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM transactions WHERE category=?",
        (category,)
    )

    connection.commit()

    connection.close()

    