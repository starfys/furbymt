import espeak
import sys
import os
import subprocess
import signal

#es = espeak.ESpeak()
#es.voice = 'en-us'
#es.speed = 300

#defaultPitch = es.pitch

def say( sayString , pit=50):
	sp = subprocess.Popen(['espeak', sayString])
	print('PID is ' + str(sp.pid))
	return sp.pid

#os.kill(thisPid, signal.SIGTERM)
