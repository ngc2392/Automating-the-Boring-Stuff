#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import webbrowser
import sys
import pyperclip
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
	print("The address passed in is: " + address)
else:
	address = pyperclip.paste()
	print("The address taken from the clipboard: " + address)

webbrowser.open('https://www.google.com/maps/place/' + address)


