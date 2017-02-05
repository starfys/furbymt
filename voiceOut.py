import espeak
import sys
import os

es = espeak.ESpeak()
es.voice = 'en-us'
#es.speed = 300

defaultPitch = es.pitch

def say( str , pit=defaultPitch):
	tempPit = es.pitch
	es.pitch = pit
	es.say(str)
	es.pitch = tempPit
	return pid