import tkinter
import math

global calculation

tk = tkinter.Tk()
tk.title('Calculator')
tk.geometry('435x600')


h = 1
w = 4

calculation = ''
output = tkinter.StringVar()
output.set('0')



def addToDisplay(char):
    global calculation
    calculation += str(char)
    output.set(calculation)

def delFun():
    global calculation
    calculation = calculation[:-1]
    output.set(calculation)

def clrFun():
    global calculation
    calculation = ''
    output.set(calculation)

def calculate():
    global calculation
    

display = tkinter.Label(tk, textvariable=output, font=('Sans Serif',64))

display.grid(row=0, columnspan=5, sticky='e')

tkinter.Button(tk, text='PI', font=('Sans Serif',32), height=h, width=w, command=lambda: addToDisplay(3.1416)).grid(row=2, column=1)
tkinter.Button(tk, text='x^2', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('^2')).grid(row=2, column=2)
tkinter.Button(tk, text='CLR', font=('Sans Serif',32), height=h, width=w,command=lambda:clrFun()).grid(row=2, column=3)
tkinter.Button(tk, text='DEL', font=('Sans Serif',32), height=h, width=w,command=lambda:delFun()).grid(row=2, column=4)

tkinter.Button(tk, text='(', font=('Sans Serif',32), height=h, width=w, command=lambda: addToDisplay('(')).grid(row=3, column=1)
tkinter.Button(tk, text=')', font=('Sans Serif',32), height=h, width=w, command=lambda: addToDisplay(')')).grid(row=3, column=2)
tkinter.Button(tk, text='n!', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('!')).grid(row=3, column=3)
tkinter.Button(tk, text='X', font=('Sans Serif',32), height=h, width=w, command=lambda: addToDisplay('x')).grid(row=3, column=4)


tkinter.Button(tk, text='7', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('7')).grid(row=4, column=1)
tkinter.Button(tk, text='8', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('8')).grid(row=4, column=2)
tkinter.Button(tk, text='9', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('9')).grid(row=4, column=3)
tkinter.Button(tk, text='/', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('/')).grid(row=4, column=4)

tkinter.Button(tk, text='4', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('4')).grid(row=5, column=1)
tkinter.Button(tk, text='5', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('5')).grid(row=5, column=2)
tkinter.Button(tk, text='6', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('6')).grid(row=5, column=3)
tkinter.Button(tk, text='-', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('-')).grid(row=5, column=4)

tkinter.Button(tk, text='1', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('1')).grid(row=6, column=1)
tkinter.Button(tk, text='2', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('2')).grid(row=6, column=2)
tkinter.Button(tk, text='3', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('3')).grid(row=6, column=3)
tkinter.Button(tk, text='+', font=('Sans Serif',32), height=h, width=w,command=lambda: addToDisplay('+')).grid(row=6, column=4)

tkinter.Button(tk, text='+/-', font=('Sans Serif',32), height=h, width=w,command=lambda:addToDisplay('+/-')).grid(row=7, column=1)
tkinter.Button(tk, text='0', font=('Sans Serif',32), height=h, width=w).grid(row=7, column=2)
tkinter.Button(tk, text='.', font=('Sans Serif',32), height=h, width=w).grid(row=7, column=3)
tkinter.Button(tk, text='=', font=('Sans Serif',32), height=h, width=w).grid(row=7, column=4)





tk.mainloop()