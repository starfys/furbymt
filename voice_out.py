import espeak, sys, string, os
es = espeak.ESpeak()

es.say(os.system(sys.argv[1]))