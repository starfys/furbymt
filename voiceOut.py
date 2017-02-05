import espeak
import sys
import os
import subprocess
import signal

def say( sayString , pit=50):
	sp = subprocess.Popen(['espeak', sayString])
	print('PID is ' + str(sp.pid))
	return sp.pid

