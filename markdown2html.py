#!/usr/bin/python3
"""
script that takes 2 arguments
"""
import sys
from os import path


if __name__ == "__main__":
    # Check for Usage
    if len(argv) != 3:
        eprint("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    elif not path.exists(argv[1]):
        eprint("Missing {}".format(argv[1]))
        exit(1)
    else:
        sys.exit(0)
