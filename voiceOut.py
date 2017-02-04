import espeak
import sys

es = espeak.ESpeak()
es.voice = 'en-us'
#es.speed = 300

def say( str ):
	es.say(str)
	return