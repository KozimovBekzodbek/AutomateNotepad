import os
import sys

task_name = "Automate_Notepad_Task"

base_dir = os.path.dirname(os.path.abspath(__file__))
venv_python = os.path.join(base_dir, "venv", "Scripts", "python.exe")
script_path = os.path.join(base_dir, "auto.py")

command = f'schtasks /create /tn "{task_name}" /tr "{venv_python} {script_path}" /sc daily /st 16:10 /f'

os.system(command)

print(f"✅ Task '{task_name}' successfully added to Windows Task Scheduler!")
