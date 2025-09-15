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

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"{task['Id']}. {task['description']}      {task['status']}")

def delete_tasks(Id):
    tasks = load_tasks()
    if Id in range(len(tasks) + 1):
        for task in tasks:
            if task['Id'] == Id:
                tasks.remove(task)
        for index, task in enumerate(tasks, start=1):
            task['Id'] == index
        save_tasks(tasks)
        print("Task deleted")
    else:
        print("Task not found")

def main():
    parser = argparse.ArgumentParser(description="A Task Tracking App")
    subparsers = parser.add_subparsers(dest='command', help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", description="Adds a given task")
    add_parser.add_argument("description", type=str, help="Task description")

    # Update command
    update_parser = subparsers.add_parser("update", description="Updates a tasks status")
    update_parser.add_argument("Id",help="update parser")

    # Delete command
    delete_parser = subparsers.add_parser("delete", description="Deletes a chosen task")
    delete_parser.add_argument("Id", type=int, help="Task Id")

    # List command
    list_parser = subparsers.add_parser("list",description="Listing all tasks")
    list_parser.add_argument("list", type=str, nargs='?', default=None, help="List tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_tasks(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "delete":
        delete_tasks(args.Id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()