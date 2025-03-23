import os




task_name = "Notepad Automation"

base_dir = os.path.dirname(os.path.abspath(__file__))

venv_python = os.path.join(base_dir, "venv", "Scripts", "python.exe")

script_path = os.path.join(base_dir, "auto.py")

command = f'schtasks /create /tn "{task_name}" /tr "cmd.exe /c cd /d {base_dir} && {venv_python} {script_path}" /sc daily /st 10:10 /f'




os.system(command)
