import os

# returns the command line time in a string
def time():
	t = "The time is "
	f = os.popen('date +%r')
	t += f.read()

	return (str(t))