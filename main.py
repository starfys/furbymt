#!/bin/python3
#Import furby output function
from voiceOut import say 
import fileinput
import threading
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

def modSelect(str):
	firstword = str.split()[0]
	theRest = ''
	for word in str.split()[1:]:
		theRest = theRest + word + ' '
	if firstword == "bee":
		say(bee(), 0)
	elif firstword == "compute": 
		say(math(theRest), 0)
	elif firstword == "love": 
		say(love(), 0)
	elif firstword == "date":
		say(date(), 0)
	elif firstword == "query":
		say(wolfram(theRest), 0)
	elif firstword == "fortune":
		say(fortune(), 0)
	elif firstword == "lucky": #takes arguments
		say(lucky(theRest), 0) 
	elif firstword == "stallman":
		say(stallman(), 0)
	elif firstword == "time":
		say(get_time(), 0)
	elif firstword == "weather":
		say(weather(), 0)
	elif firstword == "forecast": #takes arguments
		print(theRest)
		say(get_forecast(theRest), 0)
	else:
   		say("You said "+ str + ". Command not recognized. Did you mean to say, Furby, self destruct?.", 13)


class furby_sayThread (threading.Thread):
	def __init__(self, threadID, name, mod):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.mod = mod

	def run(self):
	#	print( "Starting " + self.name)
		modSelect(self.mod)
	#	print ("Exiting " + self.name)
	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()


#say("Furby online.", 500)

while True:
	val = input('Do? ')
	for thread in threads:
		if not thread.is_alive():
			print ("Removed finished thread.")
			threads.remove(thread)
	if len(threads) > 0:
		if val == "quit" or val == "shut up" or val == "exit" or val == "quiet":
			sayThread.stop()
			print("Thread told to stop.")
			#sayThread = furby_sayThread(1, "sayThread", "quit")
			#sayThread.start( )
			#threads.append(sayThread)
		else:
			print("Thread told to restart.")
			sayThread = furby_sayThread(1, "sayThread", val)
			sayThread.start( )
			threads.append(sayThread)
	else:
			print("Nothing running, starting new thread.")
			sayThread = furby_sayThread(1, "sayThread", val)
			sayThread.start( )
			threads.append(sayThread)
	print (threads) 

'''
	if len(threads) > 0:
		if val == "quit" or val == "shut up" or val == "exit" or val == "quiet":
			threads[0].stop()
		elif threads[0].name == 'sayThread':
			pass
		else:
			sayThread = furby_sayThread(1, "sayThread", val)
			sayThread.start( )
			threads.append(sayThread)
	else:
			sayThread = furby_sayThread(1, "sayThread", val)
			sayThread.start( )
			threads.append(sayThread)
	print (threads) 


	if val == 'time':
		sayThread.mod = "time"

	elif val == 'weather':
		sayThread.mod = "weather"
		sayThread.start( )
		threads.append(sayThread)
	elif val == 'date':
		pass
	else:
		say("You are making me angry.", 0)'''
#
#		elif:
#
#		elif:	'''
