import pyautogui
import time
time.sleep(5)
for i in range(1,5):
    pyautogui.write('Hello World',interval=0.25)
    pyautogui.press("enter")

