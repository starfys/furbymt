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


def modSelect(str):
	pass
	


class furby_sayThread (threading.Thread):
	def __init__(self, threadID, name, mod):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.mod = mod
	def run(self):
	#	print( "Starting " + self.name)
		say(self.mod, 0)
	#	print ("Exiting " + self.name)

threadLock = threading.Lock()
threads = []


def furby_say(string):
	
	return
def furby_show():
	return
def furby_move():
	return

while True:
	val = input('Do? ')

	sayThread = furby_sayThread(1, "sayThread", val)
	sayThread.start( )
	threads.append(sayThread)

	'''if val == 'time':
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
#		elif:	