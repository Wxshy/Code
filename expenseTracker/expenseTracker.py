import sqlite3

from  tkinter import *

import time
from tkcalendar import *

db = 'expenses.sql'

conn = sqlite3.connect(db)

tk = Tk()
tk.title('Expense Tracker')
tk.geometry('600x400')


def addExpense():
    
    def submitData():
        
        amount = amountInput.get()
        date = DateInput.get_date()
        item = itemInput.get()
        print(amount, date, item)

        c = conn.cursor()

        sql = '''INSERT INTO Expenses VALUES (?,?,?,?);'''
        d = [None,amount, date, item]
        c.execute(sql,d)
        c.commit()

        tk.destroy()

    tk =  Tk()
    tk.title('Add Expense')
    tk.geometry('600x400')

    amtText =  Label(tk, text='Amount:').pack()
    amountInput =  Entry(tk)
    amountInput.pack()

    DateInput = Calendar(tk, selectmode='day')
    DateInput.pack(pady=20)

    itemText = Label(tk, text='Item:').pack()
    itemInput = Entry(tk)
    itemInput.pack()

    submit = Button(tk, text='Submit', command=submitData).pack()

title =  Message(tk, text='Expense Tracker', font=48).pack()
add_expesne_button =  Button(tk, text='Add Expense', command=addExpense, font=40).pack()

tk.mainloop()
