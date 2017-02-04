import espeak
import sys



arg1 = input()

es = espeak.ESpeak()
es.say(arg1)