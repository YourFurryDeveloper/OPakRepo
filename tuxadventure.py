#!/usr/bin/env python3
import argparse
import sys
import os
import time

# Create the main parser
parser = argparse.ArgumentParser(prog='tuxadventure', description="A fun little text-based terminal game with the Linux mascot, Tux as the star of the show :)")

# Create subparsers for the subcommands
subparsers = parser.add_subparsers(dest='command')

# Parse the arguments
args = parser.parse_args()

def typing_effect(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensures the character is displayed immediately
        time.sleep(speed)  # Controls how fast the typing happens
    print()

global money
global health
global level
money = 5
health = 100
level = 0

global inventory
inventory = ["Health Potion"]

def showOptScr(prompt, correct_prompt):
	print("Health: " + str(health)+ " | Money: " + str(money) + " | Level: " + str(level))
	print("----------\n \n")
	typing_effect(prompt + "\n \n \n", speed=0.05)
	print("(i)nventory, (q)uit \n \n")
	usr_input = input("> ")
	
os.system("clear")
global usrname
usrname = input("What is your name? > ")
time.sleep(0.5)
os.system("clear")
typing_effect("Well, welcome to your adventure, " + usrname + "!", speed=0.05)
input("")
typing_effect("You will be traveling through the world of Linux as the Linux mascot, Tux! (I think that makes you a furry, too lol so haha)", speed=0.05)
input("")
typing_effect("Well, I think that's all for now, happy adventuring and good luck!", speed=0.05)
input("")
os.system("clear")
time.sleep(0.5)
showOptScr("You wake up in the depths of Linux, with a system to construct. You first need to send a command that will update the package lists, so everything is ready to go. Type it in the box below OR type an inventory command.", "sudo apt update")

