import tkinter
import pyperclip
 
tk = tkinter.Tk()

def getValues():
    rv = rslider.get()
    gv = gslider.get()
    bv = bslider.get()

    rvh = hex(rv)[2:]
    gvh = hex(gv)[2:]
    bvh = hex(bv)[2:]


    if rvh == '0':
        rvh = '00'
    
    if len(rvh) == 1:
        rvh += '0'

    if gvh == '0':
        gvh = '00'

    if len(gvh) == 1:
        gvh += '0'

    if bvh == '0':
        bvh = '00'
    
    if len(bvh) == 1:
        bvh += '0'

    

    hexbg = '#' + rvh + gvh + bvh


    tk.config(bg = hexbg)

    if rv < 70 and gv < 70 and bv < 70:
        rslider.config(fg = 'white')
        gslider.config(fg = 'white')
        bslider.config(fg = 'white')
        showval.config(fg = 'white')

    else:
        rslider.config(fg = 'black')
        gslider.config(fg = 'black')
        bslider.config(fg = 'black')
        showval.config(fg = 'black')

    rslider.config(bg = hexbg)
    gslider.config(bg = hexbg)
    bslider.config(bg = hexbg)
    showval.config(text = hexbg, bg = hexbg)

    return hexbg


rslider = tkinter.Scale(tk, from_=0, to=255)
gslider = tkinter.Scale(tk, from_=0, to=255)
bslider = tkinter.Scale(tk, from_=0, to=255)

rslider.pack()
gslider.pack()
bslider.pack()

confirm = tkinter.Button(tk, text='CONFIRM', command=getValues)
confirm.pack()

showval = tkinter.Label(tk, text='')
showval.pack()

def cf():
    ttc = getValues()
    pyperclip.copy(ttc)

copy = tkinter.Button(tk, text='COPY', command=cf)
copy.pack()

tk.mainloop()