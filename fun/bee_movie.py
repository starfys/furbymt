# returns the bee movie script as a string from the file bee
def bee():
	file = open('bee','r')
	script = file.read()
	return(str(script))