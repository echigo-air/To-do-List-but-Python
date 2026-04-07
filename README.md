# 📋 Tasklog – a terminal to-do list

A simple, no‑distraction to‑do list that runs in your terminal.  
Tasks survive between sessions. No account. No ads. No notifications. Just you and what needs to be done.

## ✨ Features

- add, view, and delete tasks
- tasks are saved to a local file
- clean terminal interface with screen clearing
- loading animation on start (because why not)

## 🚀 Getting started

### requirements
- Python 3.13 or higher
- works on Windows, macOS, Linux, and Termux (Android)

### Run It

```bash
python tasklog.py
```
No installation. No dependencies outside the standard library.

🎮 How to Use
```
1. Add Task
2. See Tasks
3. Remove Task
4. Quit
```
Type the number of what you want to do. That's it.

🧠 Why I Built This
i wanted something that feels like mine. no AI wrote the code. just my brain, my phone (acode + termux), and a few late nights.

this is the first real thing i've finished. it's small. it's simple. but it works.

📁 File Structure
text
```tasklog/
├── tasklog.py      # main script
└── tasks.txt       # created automatically – stores your tasks
```
🛠️ Built With
python 3.13.7

os, time, sys – only the standard library

my own patience (and lack of it)

📝 Notes
tasks are stored in plain text. you can edit tasks.txt manually if you want.

the loading animation runs every time you start the program. it's dramatic for no reason. i like it. (also kinda bug you can just fix it or not)

"it's messy but it's mine."
