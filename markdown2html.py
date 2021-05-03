#!/usr/bin/python3
"""
script that takes 2 arguments
"""
import sys
from os import path


if __name__ == "__main__":
    """
    a function that turns markdown to html 
    """
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    elif not path.exists(sys.argv[1]) or not sys.argv[1].endswith('.md'):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        sys.exit(1)
    else:
        sys.exit(0)
