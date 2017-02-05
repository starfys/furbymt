from random import randint

def love():
		heart = randint(0,3)
		if(heart == 0):
			return ("I don't like you!")
		if(heart == 1):
			return ("I'm putting you in the friend zone!")
		if(heart == 2):
			return ("You're my best friend")
		if(heart == 3):
			return ('I love you too!')