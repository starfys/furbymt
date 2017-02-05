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

import speech_recognition as sr
import requests
import json
from voiceOut import say
# obtain audio from the microphone
r = sr.Recognizer()
r.energy_threshold=1000

def get_command():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        tts_result = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #Read keys from json
    with open('keys.json','r') as keys_file:
        keys = json.load(keys_file)
    apiai_client_token = keys['apiai_client_token']
    #Create a session
    session = requests.Session()
    session.headers.update({"Authorization":"Bearer {}".format(apiai_client_token),
	                    "Content-Type":"application/json; charset=utf-8"})
    #API.ai
    API_BASE_URL="https://api.api.ai/v1/"
    #Make a request
    return session.get(API_BASE_URL+"query", params={"query": tts_result,"v":"20170204","sessionId":"furby","lang":"en"}).json()["result"]


threadLock = threading.Lock()
threads = []
currentPid = -1

def modSelect(thisString):
	global currentPid
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
	currentPid = thisPid
	return thisPid

class furby_sayThread (threading.Thread):
	def __init__(self, threadID, name, mod):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.mod = mod

	def run(self):
		currentPid = modSelect(self.mod)
#	def stop(self):
#		self._stop.set()

#	def stopped(self):
#		return self._stop.isSet()

mainPid = os.getpid()

while True:
	currentPid = 0

	dic = get_command()
	val = dic['action']
	
	print(val)
	if len(threads) > 0:
		if val == "quit" or val == "stop" or val == "shut up" or val == "exit" or val == "quiet":
			if not currentPid == mainPid :
				os.kill(currentPid, signal.SIGTERM)

			for thread in threads:
				if not thread.is_alive():
					threads.remove(thread)
		else:
			os.kill(currentPid, signal.SIGTERM)
			sayThread = furby_sayThread(1, "sayThread", val)
			sayThread.start( )
			threads.append(sayThread)
			for thread in threads:
				if not thread.is_alive():
					threads.remove(thread)

	else:
			if val == "quit" or val == "shut up" or val == "exit" or val == "quiet":
				os.kill(currentPid, signal.SIGTERM)
			sayThread = furby_sayThread(1, "sayThread", val)
			sayThread.start( )
			threads.append(sayThread)