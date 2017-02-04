#Import voice output function
from voice_out import say

# Import modules
from bee_movie import bee
from date import date
from fortune import fortune
from lucky_number import lucky
from richard_stallman import stallman
from time import time
from weather import weather

print("Weather...")
#say(weather())

print("Lucky...")
#say(lucky("aeuaoeu"))
print("Date...")
#say(date())
print("Fortune...")
#say(fortune())
print("Time...")
print(time())
print("Stallman...")
say(stallman())
#print("Bee...")
#say(bee())