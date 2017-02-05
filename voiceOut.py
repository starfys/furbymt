import espeak
import sys
import os
import subprocess
import signal

def say( sayString , pit=50):
	sp = subprocess.Popen(['espeak', sayString])
	return sp.pid

