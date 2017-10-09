Pass in an address from the command line.  Go to the directory where the script is located.  Run ./scriptname address 
You don't need to include python or python3 in the beginning if you include a shebang that points to the proper python interpreter

If no arguments are passed in, then it will be assumed that the user copied the address onto their clipboard.  The pyperclip package is used to access the clipboard.  To install pyperclip run the command: pip install pyperclip --user 
