import pyautogui
import time
import os

print("Script ishlayapti! Notepad ochilyapdi.")

with open("count.txt", "r") as f:
     num = int(f.read())

os.system("notepad.exe")

time.sleep(2)  

pyautogui.hotkey('ctrl', 't')

time.sleep(1)  

pyautogui.write("This is an automated test.\nHello World!", interval=0.1)

time.sleep(1)

pyautogui.hotkey('ctrl', 's')
time.sleep(1)

pyautogui.write(f"auto_{num}.txt")
time.sleep(1)

with open("count.txt", "w") as f:
    f.write(f"{num+1}")

pyautogui.press('enter')
time.sleep(1)

pyautogui.hotkey('alt', 'f4')
time.sleep(1)


os.system("exit") 
