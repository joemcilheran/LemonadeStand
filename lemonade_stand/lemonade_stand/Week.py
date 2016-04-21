import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Bank
import Recipe
import Purchases
import Player
from decimal import *
getcontext().prec = 4

class Week:

    def __init__(self):
        
        player = Player.Player()
        chance = Chance.Chance()
        dayCounter = 0
        servedCustomers = 0
        satisfiedCustomers = 0
        popularity = 0
   
    def run_week(self):        
        while dayCounter < 7:
            day = Day.Day()
            day = day.run_day(week,
            
                   
    def find_popularity(self):
        if servedCustomers == 0:
            popularity = popularity
        else:
            popularity = Decimal(satisfiedCustomers / servedCustomers)
        return popularity
          