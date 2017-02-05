#!/bin/python3
#Import furby output function
from voiceOut import say 
import fileinput
import threading
import os
import subprocess
import signal
#from movementOut import move
#from screenOut import display

# Import modules
from furby_beeMovie import bee
from furby_math import math
from furby_date import date
from furby_fortune import fortune
from furby_luckyNumber import lucky
from furby_richardStallman import stallman
from furby_time import get_time
from furby_weather import weather
from furby_forecast import get_forecast
from furby_inspire import inspire
from furby_wolfram import wolfram
from furby_love	import love

threadLock = threading.Lock()
threads = []
currentPid = -1

def modSelect(thisString):
	global currentPid
	print('UEOUOE ' + str(currentPid))
	if thisString == '':
		return
	firstword = thisString.split()[0]
	theRest = ''
	for word in thisString.split()[1:]:
		theRest = theRest + word + ' '
	if firstword == "bee":
		thisPid = say(bee(), 0)
	elif firstword == "compute": 
		thisPid = say(math(theRest), 0)
	elif firstword == "love": 
		thisPid = say(love(), 0)
	elif firstword == "date":
		thisPid = say(date(), 0)
	elif firstword == "query":
		thisPid = say(wolfram(theRest), 0)
	elif firstword == "fortune":
		thisPid = say(fortune(), 0)
	elif firstword == "lucky": #takes arguments
		thisPid = say(lucky(theRest), 0) 
	elif firstword == "stallman":
		thisPid = say(stallman(), 0)
	elif firstword == "time":
		thisPid = say(get_time(), 0)
	elif firstword == "weather":
		thisPid = say(weather(), 0)
	elif firstword == "torture":
		thisPid = say("Aaaaaaaaaaaaaaaaaoeeeeeeaaaaaaaaaaaaagggggll", 0)
	elif firstword == "forecast": #takes arguments
		thisPid = say(get_forecast(3), 0)
	else:
		thisPid = say("You said "+ thisString + ". Command not recognized. Did you mean to say, Furby, self destruct?.", 13)
	print('RETURNING ' + str(thisPid))
	currentPid = thisPid
	return thisPid

class furby_threadWait (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
#		self.threadID = threadID
#		self.name = name
#		self.mod = mod

	def run(self):
		while True:
		#	print(currentPid)
			for thread in threads:
				if not thread.is_alive():
					print ("Removed finished thread.")
					threads.remove(thread)
	#	print( "Starting " + self.name)
	#	print("My pid: " + str(os.getpid()))
	#	currentPid = modSelect(self.mod)
	#	print ("Exiting " + self.name)
#	def stop(self):
#		self._stop.set()

#	def stopped(self):
	#	return self._stop.isSet()	

class furby_sayThread (threading.Thread):
	def __init__(self, threadID, name, mod):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.mod = mod

	def run(self):
	#	print( "Starting " + self.name)
		print("My pid: " + str(os.getpid()))
		currentPid = modSelect(self.mod)
		print('I GOT ' + str(currentPid))
	#	print ("Exiting " + self.name)
#	def stop(self):
#		self._stop.set()

#	def stopped(self):
#		return self._stop.isSet()


#say("Furby online.", 500)
print("Main pid: " + str(os.getpid()))
mainPid = os.getpid()
#waitThread = furby_threadWait()
#waitThread.start()

while True:
	currentPid = 0

	val = input('Do? ')
	#for thread in threads:
	#	if not thread.is_alive():
	#		print ("Removed finished thread.")
	#		threads.remove(thread)

	if len(threads) > 0:
		if val == "quit" or val == "stop" or val == "shut up" or val == "exit" or val == "quiet":
			#sayThread.stop()
			print("Thread told to stop.")
			if not currentPid == mainPid :
				os.kill(currentPid, signal.SIGTERM)
			print('KILLING ' + str(currentPid))
			#sayThread = furby_sayThread(1, "sayThread", "quit")
			#sayThread.start( )
			#threads.append(sayThread)
			for thread in threads:
				if not thread.is_alive():
					print ("Removed finished thread.")
					threads.remove(thread)
		else:
			print("Thread told to restart.")
			os.kill(currentPid, signal.SIGTERM)
			print('KILLING ' + str(currentPid))
			sayThread = furby_sayThread(1, "sayThread", val)
			sayThread.start( )
			print('NOW ITS ' + str(currentPid))
			threads.append(sayThread)
			for thread in threads:
				if not thread.is_alive():
					print ("Removed finished thread.")
					threads.remove(thread)

	else:
			if val == "quit" or val == "shut up" or val == "exit" or val == "quiet":
				os.kill(currentPid, signal.SIGTERM)
			print("Nothing running, starting new thread.")
			sayThread = furby_sayThread(1, "sayThread", val)
			sayThread.start( )
			print('NOW ITS ' + str(currentPid))
			threads.append(sayThread)
	print (threads) 