import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.001
button = Button.left
master_key = KeyCode(char='s')
exitk = KeyCode(char='q')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.prunning = True

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def exit(self):
        self.stop()
        self.prunning = False

    def run(self):
         while self.prunning:
             while self.running:
                 mouse.click(self.button)
                 time.sleep(self.delay)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == master_key:
        if click_thread.running:
            click_thread.stop()
        else:
            click_thread.start()
    elif key == exitk:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()       
