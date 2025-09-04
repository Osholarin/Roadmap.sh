import argparse
import json
from datetime import datetime

filename = "tasks.json"

def load_tasks():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        with open(filename, 'w') as file:
            json.dump([], file, indent=2)
        
def add_tasks(description, status="pending"):
    tasks = load_tasks()
    task_dict = {
        'Id': len(tasks) + 1,
        'description': description,
        'status': status,
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task_dict)
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=2)
    print(f"Task added: {task_dict['description']}")


def main():
    parser = argparse.ArgumentParser(description="A Task Tracking app")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Adds a given task")
    add_parser.add_argument('description', type=str, help='Task description')

    args = parser.parse_args()

    if args.command == "add":
        add_tasks(args.description)

if __name__ == "__main__":
    main()