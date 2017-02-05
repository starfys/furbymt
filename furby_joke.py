from random import choice

# haha funny funny
def pun():
	jokes = [line.rstrip('\n') for line in open('furby_dadJokes.dat')]
	return(str(choice(jokes)))

print(pun())