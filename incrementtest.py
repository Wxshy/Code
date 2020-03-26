import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from functools import partial
global num1,num2
num1 = 0
num2 = 0

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 2


        self.lab = Label(text=str(num1))
        self.add_widget(self.lab)
        self.lab2 = Label(text=str(num2))
        self.add_widget(self.lab2)

        self.add1 = Button(text="NUM1")
        self.add1.bind(on_press=partial(self.addf, 'num1'))
        self.add_widget(self.add1)
        self.add2 = Button(text="NUM2")
        self.add2.bind(on_press=partial(self.addf, 'num2'))
        self.add_widget(self.add2)

    def addf(self, instance, att):
        global num1, num2
        if att == 'num1':
            num1 += 1
            print(num1)        





class TestApp(App):
    def build(self):
        return Grid()

if __name__ == "__main__":
    TestApp().run()