#!/bin/python3
#Import furby output function
from voiceOut import say 
import fileinput
import threading
import os
import subprocess
import signal
import random
from random import randrange


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
from furby_love    import love

import speech_recognition as sr
import requests
import json
from voiceOut import say
# obtain audio from the microphone
r = sr.Recognizer()
r.energy_threshold=1000

def error_func(thisString):
   error = randrange(0, 4, 1)
   if error == 0:
       thisPid = say(thisString + "does not compute!", 13)
   elif error == 1:
       thisPid = say("You said "+ thisString + ". Command not recognized. Did you mean to say, Furby, self destruct?.", 13)
   elif error == 2:
       thisPid = say("I do not understand you.", 13)
   elif error == 3:
       thisPid = say("I'm not picking up what you are putting down here!", 13)
   else:
       thisPid = say("You said "+ thisString + ". Command not recognized.", 13)


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
        print('Got ' + tts_result)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
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
def get_query():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        tts_result = r.recognize_google(audio)
        print('Got ' + tts_result)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
    return tts_result

threadLock = threading.Lock()
threads = []
currentPid = -1

queries = ['Yes?', 'I\'m listening.', 'Go ahead.', 'Ask away.', 'I\'m sworn to carry your burdens.', 'I have an answer.', 'What?', 'Mmhmm?', 'Mmyes?']

def modSelect(thisString):
    global currentPid
    if thisString == '':
        return
    firstword = thisString
    if firstword == "compute": 
        thisPid = say(math(theRest), 0)
    elif firstword == "get_love": 
        thisPid = say(love(), 0)
    elif firstword == "prompt_question": 
        thisPid = say(random.choice(queries), 0)
        dic = get_query()
        if dic is not None:
            say(wolfram(dic))
        else:
            say("query failed")
    elif firstword == "get_date":
        thisPid = say(date(), 0)
    elif firstword == "query":
        thisPid = say(wolfram(theRest), 0)
    elif firstword == "get_fortune":
        thisPid = say(fortune(), 0)
    elif firstword == "lucky": #takes arguments
        thisPid = say(lucky(theRest), 0) 
    elif firstword == "get_stallman":
        thisPid = say(stallman(), 0)
    elif firstword == "get_time":
        thisPid = say(get_time(), 0)
    elif firstword == "weather":
        thisPid = say(weather(), 0)
    elif firstword == "torture":
        thisPid = say("Aaaaaaaaaaaaaaaaaoeeeeeeaaaaaaaaaaaaagggggll", 0)
    elif firstword == "forecast": #takes arguments
        thisPid = say(get_forecast(3), 0)
    else:
        error_func(thisString)
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
#    def stop(self):
#        self._stop.set()

#    def stopped(self):
#        return self._stop.isSet()

mainPid = os.getpid()

while True:
    currentPid = 0
    say("What is your command?")
    dic = get_command()
    if dic is None:
        continue
    try:
        val = dic['action']
    except:
        val = dic['resolvedQuery']
    print(val)
    modSelect(val)
