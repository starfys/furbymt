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


def _async_raise(tid, exctype):
    '''Raises an exception in the threads with id tid'''
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,
                                                  ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # "if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")

class ThreadWithExc(threading.Thread):
    '''A thread class that supports raising exception in the thread from
       another thread.
    '''

    def __init__(self, threadID, name, mod):
        super(StoppableThread, self).__init__()
        self.threadID = threadID
        self.name = name
        self.mod = mod
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def _get_my_tid(self):
        """determines this (self's) thread id

        CAREFUL : this function is executed in the context of the caller
        thread, to get the identity of the thread represented by this
        instance.
        """
        if not self.isAlive():
            raise threading.ThreadError("the thread is not active")

        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id

        # no, look for it in the _active dict
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid

        # TODO: in python 2.6, there's a simpler way to do : self.ident

        raise AssertionError("could not determine the thread's id")

    def raiseExc(self, exctype):
        """Raises the given exception type in the context of this thread.

        If the thread is busy in a system call (time.sleep(),
        socket.accept(), ...), the exception is simply ignored.

        If you are sure that your exception should terminate the thread,
        one way to ensure that it works is:

            t = ThreadWithExc( ... )
            ...
            t.raiseExc( SomeException )
            while t.isAlive():
                time.sleep( 0.1 )
                t.raiseExc( SomeException )

        If the exception is to be caught by the thread, you need a way to
        check that your thread has caught it.

        CAREFUL : this function is executed in the context of the
        caller thread, to raise an excpetion in the context of the
        thread represented by this instance.
        """
        _async_raise( self._get_my_tid(), exctype )

while True:
    val = input('Do? ')
    for thread in threads:
        if not thread.is_alive():
            print ("Removed finished thread.")
            threads.remove(thread)
    if len(threads) > 0:
        if val == "quit" or val == "shut up" or val == "exit" or val == "quiet":
            sayThread.stop()
            #sayThread = ThreadWithExc(1, "sayThread", "quit")
            #sayThread.start( )
            #threads.append(sayThread)
        else:
            sayThread = ThreadWithExc(1, "sayThread", val)
            sayThread.start( )
            threads.append(sayThread)
    else:
            sayThread = ThreadWithExc(1, "sayThread", val)
            sayThread.start( )
            threads.append(sayThread)
    print (threads) 