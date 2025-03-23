from datetime import datetime
import pyautogui
import time
import os




process_list = [ "chrome.exe", "firefox.exe", "Spotify.exe", "telegram.exe", "Code.exe", "notepad.exe", "idea64.exe", "pycharm64.exe","yandex.exe", "browser.exe"]

for process in process_list:
    os.system(f"taskkill /F /IM {process}")




with open("count.txt", "r") as f:
     num = int(f.read())




os.system("notepad.exe")

time.sleep(2)  


pyautogui.hotkey('ctrl', 't')

time.sleep(1)  


pyautogui.write("Hello World", interval=0.1)

time.sleep(1)


pyautogui.hotkey('ctrl', 's')

time.sleep(1)


pyautogui.write(f"auto_{num}.txt")

time.sleep(1)



with open("log.txt", "a") as f:
    f.write(f"\n {num} - session {datetime.now()}")



with open("count.txt", "w") as f:
    f.write(f"{num+1}")



pyautogui.press('enter')

time.sleep(1)


pyautogui.hotkey('alt', 'f4')

time.sleep(1)


os.system("exit") 
