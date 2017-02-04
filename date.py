import os

# returns the command line date in a string
def date():
	d = "The date is "
	f = os.popen('date +%A')
	d += f.read()

	f = os.popen('date +%B')
	d += f.read()

	f = os.popen('date +%d')
	d += f.read()

	f = os.popen('date +%Y')
	d += f.read()

	return (str(d))
print(date())