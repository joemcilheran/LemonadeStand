import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Bank
import Recipe
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
        dayCounter = 0
        while dayCounter < 7:
            dayCounter = self.add_to_dayCounter(dayCounter)
            print ("Day Counter: " + str(dayCounter))
            day = Day.Day()
            day.run_day()
            
                   
    def find_popularity(self,day):
        if servedCustomers == 0:
            popularity = popularity
        else:
            popularity = Decimal(satisfiedCustomers / servedCustomers)
        return popularity
        
    def add_to_servedCustomers(self,day):
        servedCustomers = (servedCustomers + dailyServed)
        print(str(servedCustomers) + "servedCustomers")
        return servedCustomers
        
    def add_to_satisfiedCustomers(self,day):
        satisfiedCustomers = (satisfiedCustomers + dailySatisfied)
        print(str(satisfiedCustomers) + "satisfiedCustomers")
        return satisfiedCustomers
        
    def add_to_dayCounter(self, dayCounter):
        dayCounter = dayCounter + 1
        return dayCounter
        
    def display_day(self):
        print("Day " + str(dayCounter))
          