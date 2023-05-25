import time
import keyboard
import win32api, win32con

holdTime = 0.01

clickAtCustomPosition = False
waitTime = 0

posX = 0
posY = 0

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(holdTime)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_at_mouse_pointer():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(holdTime)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('p') == False:
    if keyboard.is_pressed('q') == False:
        if clickAtCustomPosition == False:
            click_at_mouse_pointer()
        else:
            click(posX, posY)
    time.sleep(waitTime)