import sys
import os
import subprocess
import signal

def say( sayString , pit=50):
	sp = subprocess.Popen('espeak -v en-us+f3 \"' + sayString + "\"", shell=True)
	sp.wait()
	return sp.pid

