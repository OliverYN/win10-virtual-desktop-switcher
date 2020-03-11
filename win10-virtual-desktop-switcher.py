import time,tkinter
from pynput.mouse import Button,Controller as MouseController
from pynput.keyboard import Key,Controller as KeyController

screen = tkinter.Tk()
mouse = MouseController()
keyboard = KeyController()

while True:
    x = mouse.position[0]
    if x == 0:
        keyboard.press(Key.ctrl)
        keyboard.press(Key.cmd)
        keyboard.press(Key.left)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.cmd)
        keyboard.release(Key.left)
    elif x == screen.winfo_screenwidth()-1:
        keyboard.press(Key.ctrl)
        keyboard.press(Key.cmd)
        keyboard.press(Key.right)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.cmd)
        keyboard.release(Key.right)
