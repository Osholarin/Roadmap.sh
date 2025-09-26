# Task Tracker CLI

## About 
This is a basic cli task tracking app, built in python using only modules from the standard library. It uses the textwrap and argparse library.
This is my personal implementation of the beginner python series that ia available on [roadmap.sh](https://roadmap.sh/projects/task-tracker).

#### Usage
    usage: main.py [-h] {add,update,delete,list,mark} ...

    A Task Tracking App

    positional arguments:
        {add,update,delete,list,mark}
                        Available commands

    options:
        -h, --help            show this help message and exit
    
    # Add command
    $ python main.py add "a midnight coding session"
    $ Task added
    
    # List command
    $ python main.py list
    $   ID    Description                    Status    
        -----------------------------------------------
        1     writing a solution             done      
        2     developing a solution          done      
        3     solving a problem              done      
        4     problem solving                pending   
        5     a midnight coding session      pending

#### Basic commands
* add:  This commands receives a description and saves it to a file
* list: (done , todo, in-progress) This command list all tasks or tasks with specific statuses
* update: This command updates a given task
* delete: This commands deletes a chosen task
* mark (done, in-progress) This command is used to change the status of chosen tasks
