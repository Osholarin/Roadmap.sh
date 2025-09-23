import argparse
import json
from datetime import datetime
import textwrap

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


def tabulate(id, description, status, desc_width=30):
    # wrap description text
    wrapped_desc = textwrap.fill(description, width=desc_width)
    desc_lines = wrapped_desc.split('\n')

    # Print first line with ID, first description line, and status
    print(f"{id:<5} {desc_lines[0]:<{desc_width}} {status:<10}")

    # Print remaining description lines if any
    for line in desc_lines[1:]:
        print(f"{'':5} {line:<{desc_width}} {'':10}")

def list_tasks(status=None, desc_width=30):
    tasks = load_tasks()
    print(f"{'ID':<5} {'Description':<{desc_width}} {'Status':<10}")
    print("-" * (5 + desc_width + 12))

    if status == None:
        for task in tasks:
            values = (task['Id'], task['description'], task['status'])
            tabulate(*values)

    else:
        for task in tasks:
            if task['status'] == status:
                print(f"{task['Id']}. {task['description']}      {task['status']}")

def update_tasks(Id, description):
    tasks = load_tasks()
    if Id in range(len(tasks) + 1):
        for task in tasks:
            if task['Id'] == Id:
                task['description'] = description
        save_tasks(tasks)
        print("Task updated!")
    else:
        print("Task not found!")

def delete_tasks(Id):
    tasks = load_tasks()
    if Id in range(len(tasks) + 1):
        for task in tasks:
            if task['Id'] == Id:
                tasks.remove(task)
        for index, task in enumerate(tasks, start=1):
            task['Id'] = index
        save_tasks(tasks)
        print("Task deleted")
    else:
        print("Task not found")

def mark_tasks(Id, status):
    tasks = load_tasks()
    if Id in range(len(tasks) + 1):
        for task in tasks:
            if task['Id'] == Id:
                task['status'] = status
        save_tasks(tasks)
        print(f"Task marked as {status}")
    else:
        print('Task not found!')

def main():
    parser = argparse.ArgumentParser(description="A Task Tracking App")
    subparsers = parser.add_subparsers(dest='command', help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", description="Adds a given task")
    add_parser.add_argument("description", type=str, help="Task description")

    # Update command
    update_parser = subparsers.add_parser("update", description="Updates a tasks status")
    update_parser.add_argument("Id", type=int, help="Task Id")
    update_parser.add_argument("description", type=str, help="Task description")

    # Delete command
    delete_parser = subparsers.add_parser("delete", description="Deletes a chosen task")
    delete_parser.add_argument("Id", type=int, help="Task Id")

    # List command
    list_parser = subparsers.add_parser("list",description="Listing all tasks")
    list_parser.add_argument("status", type=str, nargs='?', default=None, help="List tasks")

    # Mark commands
    mark_parser = subparsers.add_parser("mark", description="Marks tasks as finished")
    mark_parser.add_argument("Id", type=int, help="Task Id")
    mark_parser.add_argument("status", type=str, choices=['done', 'pending', 'in-progress'], help="Task status")

    args = parser.parse_args()

    if args.command == "add":
        add_tasks(args.description)
    elif args.command == "list":
        list_tasks(args.status)
    elif args.command == "delete":
        delete_tasks(args.Id)
    elif args.command == "update":
        update_tasks(args.Id, args.description)
    elif args.command == "mark":
        mark_tasks(args.Id, args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()