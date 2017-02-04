#Import furby output function
from voiceOut import say
#from movementOut import move
#from screenOut import display

# Import modules
#from bee_movie import bee
#from date import date
#from furby_fortune import fortune
#from lucky_number import lucky
from furby_richardStallman import stallman
#from timeFurby import get_time
#from weather import weather
#from furby_forecast import get_forecast
#from furby_time import get_time


print("Time...")
say(get_time())
say("23:40")
print("Weather...")
say(weather())
print("Lucky...")
say(lucky("aeuaoeu"))
print("Date...")
say(date())
print("Fortune...")
say(fortune())
print("Stallman...")
say(stallman())
print("Bee...")
say(bee())