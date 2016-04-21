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
            dayCounter = self.add_dayCounter()
            day = Day.Day()
            day.run_day(week)
            
                   
    def find_popularity(self,day):
        if servedCustomers == 0:
            popularity = popularity
        else:
            popularity = Decimal(satisfiedCustomers / servedCustomers)
        return popularity
        
    def add_to_servedCustomers(self,day):
        servedCustomers = (servedCustomers + dailyServed)
        return servedCustomers
        
    def add_to_satisfiedCustomers(self,day):
        satisfiedCustomers = (satisfiedCustomers + dailySatisfied)
        return satisfiedCustomers
        
    def add_to_dayCounter(self):
        dayCounter = dayCounter + 1
        return dayCounter
          