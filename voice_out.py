import espeak
import sys

es = espeak.ESpeak()

def say( str ):
	es.say(str)
	return

say("ITS WORKING, ITS WORKING")