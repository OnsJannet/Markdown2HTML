#!/usr/bin/python3
"""
script that takes 2 arguments
"""
import sys
from os import path
import re


if __name__ == "__main__":
    """
    a function that turns markdown to html 
    """
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    elif not path.exists(sys.argv[1]) or not sys.argv[1].endswith('.md'):
        sys.stderr.write("Missing {}\n".format(sys.argv[1]))
        sys.exit(1)
    else:
        html = []
        with open(sys.argv[1], 'r') as file:
            text = file.readlines()
            text[-1] = text[-1].replace('\n', '')

        with open(sys.argv[2], 'w') as file:
            for string in text:
                # convert (#) to html headings (h1 - h6)
                count = string.count('#')
                if count != 0:
                    html_replace = string.replace('#' * count + ' ', '')
                    html_replace = html_replace.replace('\n', '')
                    html_line = "<h{}>{}</h{}>\n".format(
                        count, html_replace, count)
                    html.append(html_line)
            file.writelines(html)
            sys.exit(0)
