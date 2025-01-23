#!/usr/bin/env python3
import argparse
import webview

# Create the main parser
parser = argparse.ArgumentParser(prog='pyweb', description="A simple Python web browser that can load URLs in a web window")

# Create subparsers for the subcommands
subparsers = parser.add_subparsers(dest='command')

# Add an option to specify the URL
parser.add_argument(
    '--url',  # Option flag (this can be a long or short option)
    type=str,  # Type of value expected (in this case, a string)
    help='The URL to load',  # Description of the option
    required=True  # Make it required, or set to False if optional
)

# Parse the arguments
args = parser.parse_args()

url = args.url
if not url.startswith("http://") and not url.startswith("https://"):
    url = "http://" + url  # Add http:// if missing
    webview.create_window("Web Browser", url)
    webview.start()
