import os
import time
import random
import sys

TODO_FILE = "tasks.txt"

def loadingDisplay(totalDuration):
    endTime = time.time() + totalDuration
    i = 0
    while time.time() < endTime:
        sys.stdout.write(f"\rLoading{'.' * (i % 4)}")
        sys.stdout.flush()
        time.sleep(0.4)
        i += 1
    print()
    clearThings()

def clearThings():
    os.system('cls' if os.name == 'nt' else 'clear')

def loadTasks():
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("No file yet. Starting fresh.")
        return []

def saveTasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def addTasks(tasks):
    newTask = input("Enter your task: ")
    tasks.append(newTask)
    saveTasks(tasks)
    print("Task added.")

def viewTasks(tasks):
    if not tasks:
        print("No task(s) yet.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def deleteTasks(tasks):
    viewTasks(tasks)
    if not tasks:
        return
    
    try:
        num = int(input("Which task number to delete? "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            saveTasks(tasks)
            print(f"You just removed: {removed}")
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter a number.")

def showMenu():
    print("\n1. Add Task")
    print("2. See Tasks")
    print("3. Remove Task")
    print("4. Quit")

tasks = loadTasks()

while True:
    clearThings()
    
    randDelay = random.randint(2, 5)

    loadingDisplay(randDelay)
    #time.sleep(randDelay)
    print(f"{randDelay}s only, somehow")
    showMenu()
    choice = input("What am I doing? ")

    if choice == "1":
        clearThings()
        addTasks(tasks)
        input("\nPress Enter to continue...")
    elif choice == "2":
        time.sleep(2)
        clearThings()
        viewTasks(tasks)
        input("\nPress Enter to continue...")
    elif choice == "3":
        time.sleep(2)
        clearThings()
        deleteTasks(tasks)
        input("\nPress Enter to continue...")
    elif choice == "4":
        clearThings()
        print("So long, nerd.")
        break
    else:
        print("Invalid choice")
        input("\nPress Enter to continue...")