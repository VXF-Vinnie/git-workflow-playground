"""A tiny command-line to-do list used to practice Git & GitHub workflows."""
import json
import sys
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))


def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    return tasks


def complete_task(tasks, index):
    tasks[index]["done"] = True
    return tasks


def format_task(index, task):
    status = "x" if task["done"] else " "
    return f"{index}. [{status}] {task['title']}"


def main(argv):
    tasks = load_tasks()
    if len(argv) < 2 or argv[1] == "list":
        for i, task in enumerate(tasks):
            print(format_task(i, task))
    elif argv[1] == "add":
        add_task(tasks, " ".join(argv[2:]))
        save_tasks(tasks)
    elif argv[1] == "done":
        complete_task(tasks, int(argv[2]))
        save_tasks(tasks)
    else:
        print("Usage: python3 todo.py [list | add <title> | done <number>]")


if __name__ == "__main__":
    main(sys.argv)
