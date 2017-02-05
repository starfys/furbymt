import espeak
import sys
import os
import subprocess

#es = espeak.ESpeak()
#es.voice = 'en-us'
#es.speed = 300

#defaultPitch = es.pitch

def say( str , pit=50):
	sp = subprocess.Popen(['espeak', '\"test\"'])
	print('PID is ' + str(sp.pid))

print("My pid: " + str(os.getpid()))
say('poo', 0)


#	tempPit = es.pitch
#	es.pitch = pit
#	es.say(str)
#	es.pitch = tempPit