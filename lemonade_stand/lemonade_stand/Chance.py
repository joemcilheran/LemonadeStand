import random
import Day
import Weather
import Customer
import Inventory
import Bank
import Recipe
import Purchases
from decimal import *
getcontext().prec = 4
import Week

class Chance:

    def __init__(self):
        pass
    
    
    def get_seventy_five_percent_chance(self):
        number = random.randint(1,4)
        if number < 4:
            return True
        else:
            return False
            
    def get_fifty_percent_chance(self):
        number = random.randint(1,4)
        if number < 3:
            return True
        else:
            return False
            
    def get_twenty_five_percent_chance(self):
        number = random.randint(1,4)
        if number == 1:
            return True
        else:
            return False