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

global isOpen
isOpen = False

def openTxt(txtfilename):
	print("PyTXT V1.0 By YourFurryDeveloper on GitHub \n")
	print("Type 'exittxt' to exit \n----------")
	isOpen = True
	lineNum = 0
	# Open the file in read mode
	with open(txtfilename, 'r') as file:
		# Loop through each line in the file
		for line in file:
			# Print the current line
			lineNum += 1
			lineNumHi = "\033[91m" + str(lineNum) + ". " + "\033[0m"
			print(lineNumHi + line.strip())  # .strip() removes leading/trailing whitespace
	# Open the file in append mode
	with open(txtfilename, 'a') as fileapp:
		while isOpen:
			txtToApp = input(lineNumHi)
			if txtToApp == "exittxt":
				os.system("clear")
				isOpen = False
			else:
				fileapp.write(txtToApp + "\n")

# Handle the subcommands
if args.command == 'open':
	os.system("clear")
	openTxt(args.file)
elif args.command == 'list':
    list_tasks()
else:
    parser.print_help()
