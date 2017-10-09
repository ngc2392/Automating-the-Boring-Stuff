#! /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4
import webbrowser
import sys

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place/' + address)


