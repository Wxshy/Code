import tkinter 
from functools import partial
import pyautogui

h, w = pyautogui.size()[0], pyautogui.size()[1]

size = str(h) + 'x' + str(w)

global passes, tackles, pcaw, pcd, carry, shots, goals

passes = 0
tackles = 0
pcaw = 0
pcd = 0
ce = 0
carry =  0
shots = 0
goals = 0

global deflect, fhit, bhit, pcag, one1

deflect = 0
fhit = 0
bhit = 0
pcag = 0
one1 = 0

tk1 = tkinter.Tk()
        

def main():
    tk1.destroy()
    tk = tkinter.Tk()
    tk.attributes('-fullscreen', True)
    tk.geometry(size)
    tk.title('Statify')

    def adder(stat):
        global passes, tackles, pcaw, pcd, ce, carry, shots, goals

        if stat == 'tackle':
            tackles += 1
            text = str('TACKLE\n' + str(tackles))
            tackleB.config(text=text)

        elif stat == 'pass':
            passes += 1
            text = 'PASS\n' + str(passes)
            passb.config(text=text)

        elif stat == 'ce':
            ce += 1
            text = 'D-ENTRY\n' + str(ce)
            ceb.config(text=text)

        elif stat == 'shot':
            shots += 1
            text = 'SHOT\n' + str(shots)
            shotb.config(text=text)

        elif stat == 'goal':
            goals += 1

            popup = tkinter.Tk()
            defb = tkinter.Button(popup, text='DEFLECTION', command=partial(goaladder, 'def'))
            fhitb = tkinter.Button(popup, text='FOREHAND', command=partial(goaladder, 'fhit'))
            bhitb = tkinter.Button(popup, text='BACKHAND', command=partial(goaladder, 'bhit'))
            pcagb = tkinter.Button(popup, text='PCA', command=partial(goaladder, 'pca'))
            one1b = tkinter.Button(popup, text='ONE ON ONE', command=partial(goaladder, '1'))

            defb.pack()
            fhitb.pack()
            bhitb.pack()
            pcagb.pack()
            one1b.pack()

            def goaladder(typpe):
                global deflect, fhit, bhit, one1
                if typpe == 'def':
                    deflect += 1
                    popup.destroy()
                elif typpe == 'fhit':
                    fhit += 1
                    popup.destroy()
                elif typpe == 'bhit':
                    bhit += 1
                    popup.destroy()
                elif typpe == 'pca':
                    pcag += 1
                    popup.destroy()
                elif typpe == '1':
                    one1 += 1
                    popup.destroy()
            
            text = 'GOAL\n' + str(goals)
            goalb.config(text=text)

        elif stat == 'pca':
            pcaw += 1
            text = 'PCA\n' + str(pcaw)
            pcab.config(text=text)

        elif stat == 'pcd':
            pcd += 1
            text = 'PCD\n' + str(pcd)
            pcdb.config(text=text)
        
        elif stat == 'carry':
            carry += 1
            text = 'CARRY\n' + str(carry)
            carryb.config(text=text)

    def opem():
        tk.attributes('-fullscreen', False)
        sw = tkinter.Tk()
        tkinter.Label(sw, text='Save before leaving?').pack() 
        
        
    
        
    tackleB = tkinter.Button(tk, text='TACKLE \n0', command=partial(adder, 'tackle') ,height=25, width=50)
    passb = tkinter.Button(tk, text='PASS \n0', command=partial(adder, 'pass'),height=25, width=50)
    ceb = tkinter.Button(tk, text='D-ENTRY \n0', command=partial(adder, 'ce'),height=25, width=50)
    shotb = tkinter.Button(tk, text='SHOT \n0', command=partial(adder, 'shot'),height=25, width=50)
    goalb = tkinter.Button(tk, text='GOAL \n0', command=partial(adder, 'goal'),height=25, width=50)
    pcab = tkinter.Button(tk, text='PCA \n0', command=partial(adder, 'pca'),height=25, width=50)
    pcdb = tkinter.Button(tk, text='PCD \n0', command=partial(adder, 'pcd'),height=25, width=50)
    carryb = tkinter.Button(tk, text='CARRY \n0', command=partial(adder, 'carry'),height=25, width=50)
    exitb = tkinter.Button(tk, text='EXIT', command=opem)

    tackleB.grid(column=1, row=1)
    passb.grid(column=2, row=1)
    ceb.grid(column=3, row=1)
    shotb.grid(column=4, row=1)
    goalb.grid(column=1, row=2)
    pcab.grid(column=2, row=2)
    pcdb.grid(column=3, row=2)
    carryb.grid(column=4, row=2)
    exitb.grid(column=6, row=1)
    
    
    tk.mainloop()
    

def menu():
    tk1.geometry(size)
    tk1.title('Statify')

    tkinter.Label(tk1, text='Statify', font='Sans').pack()

    newb = tkinter.Button(tk1, text='New Game', command=main, height=4,width=50)
    quitb = tkinter.Button(tk1, text='Quit', command=quit, height=4, width=50)

    newb.pack()
    quitb.pack()
    tk1.mainloop()

menu()

