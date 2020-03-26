import tkinter
from tkinter import *
import time

tk = tkinter.Tk()
tk.geometry('400x400')
tk.title('Counter')

idlev = 0
tokens = 0
multiplier = 1
tt = 'Tokens : 0'
multit = 'Multiplier : 1'

def auto():
    global idlev
    idlev = 0
    while True:
        time.sleep(0.5)
        idlev = idlec()
        tokens += idlev()
        tt = 'Tokens : '+str(tokens)
        ttl.configure(text=tt)
        print(tokens)


def idlec():
    global tokens, multiplier, idlec, idlev
    cost = 10*multiplier
    if tokens >= cost:
        tokens-=cost
        idlev+=1
    return idlev


def profiles():
    
    def profile(num):
        f = open('profiles.txt')
        print(f.readlines(num))


def inc():
    global tokens
    tokens += 1*multiplier
    tt = 'Tokens : '+str(tokens)
    ttl.configure(text=tt)

    



ttl = Label(tk, text=tt)
incb = Button(tk, text='Click Me!', command=inc)

upl = Label(tk, text='Upgrades:')

multib = Button(tk, text=multit, command=multic(tokens, multiplier, multit))

pt = Label(tk, text='Profiles')
p1 = Button(tk, text='1', command=profiles)

#Left Column
upl.grid(row=0,column=0)
multib.grid(row=1, column=0)

#Buffers
Label(tk,text=' ').grid(row=0,column=1)
Label(tk,text=' ').grid(row=1,column=1)
Label(tk,text=' ').grid(row=1,column=3)

#Middle Column
ttl.grid(row=0,column=2)
incb.grid(row=1,column=2)

#Right Column
pt.grid(row=0, column=4)
p1.grid(row=1, column=4)

auto()


tk.mainloop()

def multic(tokens, multiplier, multit):
    cost = 5*multiplier*2
    if tokens >= cost:
        tokens -= cost
        multiplier += 1
    

    multit = 'Mulitplyer : '+str(multiplier)
    tt = 'Tokens : '+str(tokens)
    ttl.configure(text=tt)
    multib.configure(text=multit)
    return multiplier
