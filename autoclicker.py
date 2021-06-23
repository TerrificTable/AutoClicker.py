import tkinter as tk
import win32api, win32con
import pyautogui
import keyboard
import time



window = tk.Tk()
window.title("AutoClicker by Terrific")

nothing = tk.Label(text="                                             ")
label2 = tk.Label(text="press 'q' to stop the autoclicker")

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.00000001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def clicker():
    time.sleep(2)
    while keyboard.is_pressed("q") == False:
        p = pyautogui.position()
        click(p.x, p.y)
        time.sleep(0.000000000000000000001)
    print("exiting...")
    time.sleep(0.6)
    window.destroy()
    time.sleep(2)

def destroy():
    time.sleep(1)
    window.destroy()


button = tk.Button(
    text="Start",
    width=15,
    height=2,
    bg="white",
    fg="green",
    command=clicker
)
exiting = tk.Button(
    text="Exit...",
    width=5,
    height=2,
    bg="white",
    fg="red",
    command=destroy
)


label2.pack()
nothing.pack
button.pack()
exiting.pack()
window.mainloop()
