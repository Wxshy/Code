import tkinter

tk = tkinter.Tk()
tk.geometry('250x250')

dtt = 'Mulitplier: 1'

global count
count = 0

global mt, idle
mt = 1
idle = 0
autot = 'Auto Clicker: 0'




    

def multif():
    def incmt():
        global mt
        mt += 1
    
    global dtt, mt, count
    
    mt = 1
    dtt = 'Mulitpier: ' + str(mt)
    mtlt.configure(text = dtt)
    
    if count >= 5:

        count -= 5
        incmt()
        dtt = 'Mulitplier: ' + str(mt)
        mtlt.configure(text = dtt)
        print(mt)

    dtt = 'Mulitplier: ' + str(mt)
    mtlt.configure(text = dtt)
    textt.configure(text = count)
    return dtt, mt, count

def auto():
    global count, autot
    if count >10:
        count-= 10
        idle += 1
        autot = 'Auto Clicker: '+str(idle)
        autob.configure(text = autot)
        
    return count, autot
        
    

def nClick():
    global count, mt
    count += 1*int(mt)
    textt.configure(text = count)
    while int(autot) > 0:
        count += 1*int(mt)
    print(mt, count)
    
    
    
    
ut = tkinter.Label(tk, text='Upgrades')
mtlt = tkinter.Button(tk, text = dtt, command = multif)
autob = tkinter.Button(tk, text = autot, command = auto)


textt = tkinter.Label(tk, text = count)
B = tkinter.Button(tk, text='Click Me', command=nClick)

ut.grid(column=1,row=1)
mtlt.grid(column=1,row=2)
autob.grid(column=1, row=3)
textt.grid(column=3,row=1)
B.grid(column=3,row=2)

