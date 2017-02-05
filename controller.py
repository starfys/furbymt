#!/usr/bin/env python3
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
        exit()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        exit()
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

if target_action == 'get_time':
    from furby_time import get_time
    say(get_time())
elif target_action == 'get_fortune':
    from furby_fortune import fortune
    say(fortune())
elif target_action == 'get_weather':
    from furby_weather import weather
    say(weather())
elif target_action == 'get_stallman':
    from furby_richardStallman import stallman
    say(stallman)
elif target_action == 'torture':
    say('aaaaauauuauauauauauauuauauauuaugh')
elif target_action == 'bee_movie':
    from furby_beeMovie import bee
    say(bee())
else:
    say("Command not recognized. Did you mean, Furby, self destruct?")
