import os

# returns the command line fortune in a string
def fortune():
	f = os.popen('fortune')
	now = f.read()
	return (str(now))