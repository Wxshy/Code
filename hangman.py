import tkinter


def menu():
    tk = tkinter.Tk()
    tk.title('Hangman Menu')
    tk.geometry('1920x1080')
    tk.attributes("-fullscreen",True)

    playb = tkinter.Button(tk, text='Play', font='Sans', command=main)
    playb.pack()

    quitb = tkinter.Button(tk, text='Quit', font='Sans', command=quit)
    quitb.pack()

    tk.loop()

def main():
    tk = tkinter.Tk()
    tk.title('Game')
    tk.geometry('1920x1080')
    tk.attributes("-fullscreen",True)



    

menu()