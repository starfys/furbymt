# returns the bee movie script as a string from the file bee
def bee():
	file = open('furby_bee.dat','r')
	script = file.read()
	return(str(script))