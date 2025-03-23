# Automate Notepad Task

## 📌 Overview

This project automates the process of opening Notepad, writing predefined text, and saving the file with an incremental name. It also terminates certain processes for optimization. The script is scheduled to run automatically using Windows Task Scheduler.

## 🚀 Features

- 🔹 **Process Management:** Kills unnecessary applications before execution.
- 🔹 **Automated Notepad Writing:** Opens Notepad, writes predefined text, and saves it with an incrementing filename.
- 🔹 **Task Scheduling:** Uses Windows Task Scheduler to execute the script daily at a specified time.
- 🔹 **Logging:** Maintains a log of executed sessions.

## 🛠 Installation

### 1️⃣ **Clone the Repository**

```sh
 git clone https://github.com/KozimovBekzodbek/AutomateNotepad.git
 cd AutomateNotepad
```

### 2️⃣ **Create and Activate Virtual Environment**

```sh
 python -m venv venv
 ./venv/Scripts/activate  # Windows
```

### 3️⃣ **Install Dependencies**

```sh
 pip install -r requirements.txt
```

### 4️⃣ **Set Up Task Scheduler**

```sh
 python setup.py
```

## ⚙️ How It Works

1. **Terminates processes**: Kills unwanted applications like Chrome, VS Code, Telegram, etc.
2. **Launches Notepad**: Opens Notepad and types predefined content.
3. **Saves the file**: Assigns an incrementing filename and saves it.
4. **Logs execution**: Records execution details in `log.txt`.
5. **Closes Notepad**: Exits Notepad after completion.

## 📂 Project Structure

```
📦 AutomateNotepad
 ┣ 📜 program.py        # Main script handling automation
 ┣ 📜 setup.py          # Registers the script in Task Scheduler
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 count.txt         # Stores filename increment count
 ┣ 📜 log.txt           # Execution logs
 ┣ 📜 README.md         # Documentation
```

## 🛠 Dependencies

- `pyautogui`
- `datetime`

## 🏆 Author

🔹 **Kozimov Bekzodbek**\
🔹 [**kozimovbekzodbek474@gmail.com**](mailto:kozimovbekzodbek474@gmail.com)\
🔹 **kozimov01 | KozimovBekzodbek**

## ⚠️ Disclaimer

This project is intended for educational and automation purposes only. Misuse of this script is not recommended.
