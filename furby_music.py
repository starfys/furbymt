import subprocess, signal, sys

def play(string):
    if (string == 'rick roll'):
        p = subprocess.Popen(['mpg123', '../rick.mp3'], stdout=subprocess.PIPE)
    if (string == 'cook'):
        p = subprocess.Popen(['mpg123', '../cooking.mp3'], stdout=subprocess.PIPE)
    if (string == 'kazoo'):
        p = subprocess.Popen(['mpg123', '../kazoo.mp3'], stdout=subprocess.PIPE)

#play(sys.argv[1])
