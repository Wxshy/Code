import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from functools import partial


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 2
        self.num1 = 0
        self.num2 = 0


        self.lab = Label(text=str(self.num1))
        self.add_widget(self.lab)
        self.lab2 = Label(text=str(self.num2))
        self.add_widget(self.lab2)

        self.add1 = Button(text="NUM1")
        self.add1.bind(on_press=self.addnum1)
        self.add_widget(self.add1)
        self.add2 = Button(text="NUM2")
        self.add2.bind(on_press=self.addnum2)
        self.add_widget(self.add2)

    def addnum1(self, instance):
        self.num1 += 1
        print(self.num1)
        self.lab.text = str(self.num1)
    def addnum2(self, instance):
        self.num2 += 1
        print(self.num2)
        self.lab2.text = str(self.num2)     





class TestApp(App):
    def build(self):
        return Grid()

if __name__ == "__main__":
    TestApp().run()