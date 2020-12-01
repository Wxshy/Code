import sqlite3

conn = sqlite3.connect('expenses.db')

c = conn.cursor()


c.execute('''CREATE TABLE Expenses ("expenseID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"Date"	TEXT,"Amount" REAL NOT NULL,"Item"	NUMERIC);''')

conn.commit()