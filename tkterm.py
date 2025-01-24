#!/usr/bin/env python3
import argparse
import tkinter as tk
import subprocess

# Create the main parser
parser = argparse.ArgumentParser(prog='tkterm', description="A simple terminal emulator made with Tkinter that was made ENTIRELY with ChatGPT")

# Create subparsers for the subcommands
subparsers = parser.add_subparsers(dest='command')

# Parse the arguments
args = parser.parse_args()

class TerminalEmulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Terminal Emulator")
        
        # Configure the window to resize
        self.root.geometry("800x400")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create a Text widget to display terminal output
        self.text_widget = tk.Text(root, wrap=tk.WORD, height=20, width=80, bg="black", fg="white", font=("Courier", 10))
        self.text_widget.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.text_widget.config(state=tk.DISABLED)  # Disable editing directly in the Text widget
        
        # Create an Entry widget to type commands
        self.command_entry = tk.Entry(root, bg="black", fg="white", font=("Courier", 10))
        self.command_entry.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        self.command_entry.bind("<Return>", self.execute_command)

        # Show the terminal prompt
        self.display_prompt()
        
    def display_prompt(self):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, "$ ", "prompt")
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.see(tk.END)

    def execute_command(self, event):
        command = self.command_entry.get()
        self.command_entry.delete(0, tk.END)
        
        # Display the command in the terminal
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, f"$ {command}\n", "input")
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.see(tk.END)
        
        # Check if the command is 'clear'
        if command.strip().lower() == "clear":
            self.text_widget.config(state=tk.NORMAL)
            self.text_widget.delete(1.0, tk.END)  # Clear the text area
            self.text_widget.config(state=tk.DISABLED)
            self.display_prompt()
            return
        
        try:
            # Execute the command and capture the output
            result = subprocess.run(command, shell=True, text=True, capture_output=True, check=False)
            output = result.stdout + result.stderr
        except Exception as e:
            output = str(e)

        # Display the command output
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, output + "\n", "output")
        self.text_widget.config(state=tk.DISABLED)
        self.display_prompt()
        self.text_widget.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    terminal = TerminalEmulator(root)
    root.mainloop()
