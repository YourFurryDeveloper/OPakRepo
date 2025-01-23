#!/usr/bin/env python3
import argparse
import os

# Create the main parser
parser = argparse.ArgumentParser(prog='pytxt', description="Simple text editor made with Python")

# Create subparsers for the subcommands
subparsers = parser.add_subparsers(dest='command')

# Define the 'add' subcommand
add_parser = subparsers.add_parser('open', help="Open a file")
add_parser.add_argument('file', type=str, help="Name of the file to open")

# Define the 'list' subcommand
subparsers.add_parser('list', help="List all tasks")

# Parse the arguments
args = parser.parse_args()

def openTxt(txtfilename):
	lineNum = 0
	# Open the file in read mode
	with open(txtfilename, 'r') as file:
		# Loop through each line in the file
		for line in file:
			# Print the current line
			lineNum += 1
			print(str(lineNum) + ". " + line.strip())  # .strip() removes leading/trailing whitespace

# Handle the subcommands
if args.command == 'open':
	os.system("clear")
    	openTxt(args.file)
elif args.command == 'list':
    	list_tasks()
else:
    	parser.print_help()
