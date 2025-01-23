#!/usr/bin/env python3
import argparse

# Global list to store tasks
tasks = []

def add_task(task_name):
    #"""Simulate adding a task."""
    tasks.append(task_name)
    print(f"Task '{task_name}' added.")

def list_tasks():
    #"""Simulate listing all tasks."""
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(f" - {task}")
    else:
        print("No tasks found.")

# Create the main parser
parser = argparse.ArgumentParser(prog='taskmanagersim', description="Simple task manager")

# Create subparsers for the subcommands
subparsers = parser.add_subparsers(dest='command')

# Define the 'add' subcommand
add_parser = subparsers.add_parser('add', help="Add a new task")
add_parser.add_argument('task_name', type=str, help="Name of the task to add")

# Define the 'list' subcommand
subparsers.add_parser('list', help="List all tasks")

# Parse the arguments
args = parser.parse_args()

# Handle the subcommands
if args.command == 'add':
    add_task(args.task_name)
elif args.command == 'list':
    list_tasks()
else:
    parser.print_help()
