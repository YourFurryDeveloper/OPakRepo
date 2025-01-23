#!/usr/bin/env python3
import argparse
import sys

def install_package(package_name):
    """Simulate installing a package."""
    print(f"Installing package '{package_name}'...")

# Create the main parser
parser = argparse.ArgumentParser(prog='opaktest', description="Simple package manager")

# Create subparsers for the subcommands
subparsers = parser.add_subparsers(dest='command')

# Define the 'install' subcommand
install_parser = subparsers.add_parser('install', help="Install a package")
install_parser.add_argument('package_name', type=str, help="Name of the package to install")

# Parse the arguments
args = parser.parse_args()

# Handle the install command
if args.command == 'install':
    install_package(args.package_name)
else:
    # If no subcommand or invalid subcommand, print help
    parser.print_help()
    sys.exit(1)
