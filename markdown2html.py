#!/usr/bin/python3
"""
script that takes 2 arguments
"""
import sys
from os import path
import markdown


if __name__ == "__main__":
    """
    a function that turns markdown to html 
    """
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html \n")
        exit(1)
    elif not path.exists(sys.argv[1]) or not sys.argv[1].endswith('.md'):
        sys.stderr.write("Missing" + " " + sys.argv[1] + "\n")
        exit(1)
    else:
        with open(sys.argv[1], 'r', encoding="utf-8") as file:
            text = file.read()
            html = markdown.markdown(text, extensions=['nl2br', 'sane_lists', 'legacy_attrs', 'legacy_em', 'attr_list'])
        with open(sys.argv[2], 'w', encoding="utf-8") as file:
            file.write(html)
            exit(0)
