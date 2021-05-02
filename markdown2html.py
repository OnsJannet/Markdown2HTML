#!/usr/bin/python3

import sys
from os import path
import markdown

'''
a function that turns markdown to
html and displays the files
returns exit(1) if it fails
exit(0) if it runs
'''
if __name__ == "__main__":

	if len(sys.argv) < 2:
		sys.stderr.write("Usage: ./markdown2html.py README.md README.html \n")
		exit(1)
	elif not path.exists(sys.argv[1]) or not sys.argv[1].endswith('.md'):
		sys.stderr.write("Missing" + " " + sys.argv[1] + "\n")
		exit(1)	
	else:
		with open(sys.argv[1], 'r') as file:
			text = file.read()
			html = markdown.markdown(text)
		with open(sys.argv[2], 'w') as file:
			file.write(html)
			exit(0)

