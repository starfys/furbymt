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

threadLock = threading.Lock()
threads = []

def modSelect(str):
	if str == "bee":
		say(bee(), 0)
		self.stop()
	elif str == "math":
		say(math(), 0)
	elif str == "":
		pass
	elif str == "date":
		say(date(), 0)
	elif str == "fortune":
		say(fortune(), 0)
	elif str == "inspire me":
		say(inspire(), 0)
	elif str == "lucky":
		say(lucky(), 0)
	elif str == "stallman":
		say(stallman(), 0)
	elif str == "time":
		say(get_time(), 0)
	elif str == "weather":
		say(weather(), 0)
	elif str == "forecast":
		say(get_forecast(0), 0)	
	elif str == "quit":
		say("Ok.")
	else:
   		say("You said "+ str + ". Command not recognized. Did you mean to say, Furby, self destruct?.", 13)


class furby_sayThread (threading.Thread):
	def __init__(self, threadID, name, mod):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.mod = mod
		self._stop = threading.Event()
	def run(self):
	#	print( "Starting " + self.name)
		modSelect(self.mod)
	#	print ("Exiting " + self.name)
	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()


#say("Furby online.", 500)

def furby_say(string):
	
	return
def furby_show():
	return
def furby_move():
	return

while True:
	val = input('Do? ')
	for thread in threads:
		if not thread.is_alive():
			print ("Removed finished thread.")
			threads.remove(thread)
	if len(threads) > 0:
		if val == "quit" or val == "shut up" or val == "exit" or val == "quiet":
			sayThread.stop()
			#sayThread = furby_sayThread(1, "sayThread", "quit")
			#sayThread.start( )
			#threads.append(sayThread)
		else:
			sayThread = furby_sayThread(1, "sayThread", val)
			sayThread.start( )
			threads.append(sayThread)
	else:
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