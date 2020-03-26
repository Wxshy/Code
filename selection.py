from tkinter import *

tk = Tk()

var = IntVar()

r1 = Radiobutton(tk, text='Cash',value=1,variable=var)
r1.pack()
r2 = Radiobutton(tk, text='Card',value=2,variable=var)
r2.pack()
def submit():
    print(var.get())

sub = Button(tk, text='Submit',command=submit)
sub.pack()
