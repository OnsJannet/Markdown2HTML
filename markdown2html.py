#!/usr/bin/python3

import sys
import os, fnmatch
from os import path

'''
a function that turns markdown to
html and displays the files
returns exit(1) if it fails
exit(0) if it runs
'''


if len(sys.argv) < 2:
	sys.stderr.write("Usage: ./markdown2html.py README.md README.html \n")
	exit (1)
elif not path.exists(sys.argv[1]) or not sys.argv[1].endswith('.md'):
	sys.stderr.write("Missing" + " " + sys.argv[1] + "\n")
	exit (1)
else:
	exit(0)
