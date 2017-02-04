#Import furby output function
from voiceOut import say
#from movementOut import move
#from screenOut import display

# Import modules
from furby_beeMovie import bee
from furby_date import date
from furby_fortune import fortune
from furby_luckyNumber import lucky
from furby_richardStallman import stallman
from furby_time import get_time
from furby_weather import weather
from furby_forecast import get_forecast


print("Time...")
say(get_time())

print("Weather...")
say(weather())

print("Forecast...")
say(get_forecast(0))

print("Lucky...")
say(lucky("pepe"))

print("Date...")
say(date())

print("Fortune...")
say(fortune())

print("Stallman...")
say(stallman())

print("Bee...")
say(bee())