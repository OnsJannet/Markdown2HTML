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
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html \n")
        exit(1)
    elif not path.exists(sys.argv[1]) or not sys.argv[1].endswith('.md'):
        sys.stderr.write("Missing {}".format(argv[1]))
        exit(1)
    else:
        exit(0)
