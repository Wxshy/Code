import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class Float(FloatLayout):
    number = NumericProperty()
    def __init__(self, **kwargs):
        super(Float, self).__init__(**kwargs)
        Clock.schedule_interval(self.increment_time, 0.1)
        self.increment_time(0)

    def increment_time(self, interval):
        self.number += 0.1

    def start(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, 0.1)

    def stop(self):
        Clock.unschedule(self.increment_time)



class StopwatchApp(App):
    def build(self):
        return Float()

StopwatchApp().run()