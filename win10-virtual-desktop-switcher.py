import time,tkinter
from pynput.mouse import Button,Controller as MouseController
from pynput.keyboard import Key,Controller as KeyController

screen = tkinter.Tk()
mouse = MouseController()
keyboard = KeyController()

while True:
    x = mouse.position[0]
    y = mouse.position[1]
    time.sleep(0.1)
    if x == 0 and screen.winfo_screenheight()-150 > y > 150:
        keyboard.press(Key.ctrl)
        keyboard.press(Key.cmd)
        keyboard.press(Key.left)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.cmd)
        keyboard.release(Key.left)
    elif x == screen.winfo_screenwidth()-1 and screen.winfo_screenheight()-150 > y > 150:
        keyboard.press(Key.ctrl)
        keyboard.press(Key.cmd)
        keyboard.press(Key.right)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.cmd)
        keyboard.release(Key.right)
