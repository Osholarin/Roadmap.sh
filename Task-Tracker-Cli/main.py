import argparse
import json
from datetime import datetime

filename = "tasks.json"

def load_tasks():
    while True:
        try:
            with open(filename, 'r') as file:
                tasks = json.load(file)
                return tasks
            
        except FileNotFoundError:
            save_tasks([])
            continue

def save_tasks(tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_tasks(description, status="pending"):
    tasks = load_tasks()
    task_dict = {
        "Id": len(tasks) + 1,
        "description": description,
        "status": status,
        "createdAt": datetime.now().strftime('%Y-%m-%d'),
        "updatedAt": datetime.now().strftime('%Y-%m-%d')
    }
    tasks.append(task_dict)
    save_tasks(tasks)
    print("Task added")

def main():
    parser = argparse.ArgumentParser(description="A Task Tracking App")
    subparsers = parser.add_subparsers(dest='command', help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", description="Adds a given task")
    add_parser.add_argument("description", type=str, help="Task description")

    args = parser.parse_args()

    if args.command == "add":
        add_tasks(args.description)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()