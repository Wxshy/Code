from tkinter import *
from tkinter import messagebox


def tableView():
    f = open('table.txt')
    contents = f.read()
    print(contents)













def menu():
    tk = Tk()
    tk.geometry('300x400')
    tk.configure(bg='#00F0A0')
    tk.title('League Table')


    Label(tk, text='League Table', bg = '#00F0A0', font=('Courier', 20)).pack()
    
    b1 = Button(tk, text='View', bg='#FFF080', height = 1, width = 10, command=tableView)
    b2 = Button(tk, text='Edit', bg='#FFF080', height = 1, width = 10)
    b3 = Button(tk, text='Quit', bg='#FFF080', height = 1, width = 10, command=quit)

    Label(tk, bg='#00F0A0').pack()
    b1.pack()
    b2.pack()
    b3.pack()


menu()
