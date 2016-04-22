import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Bank
from decimal import *
getcontext().prec = 4
import Week

class Recipe:

    def __init__(self):
    
        self.lemonsPerPitcher = 0
        self.sugarPerPitcher = 0
        self.icePerCup = 0
        self.lemonsPerCup = 0
        self.sugarPerCup = 0
        
    
    def get_recipe(self):
        self.add_lemons()
        self.add_sugar()
        self.add_ice()
        self.find_lemons_per_cup()
        self.find_sugar_per_cup()
    
    def add_lemons(self):
        self.lemonsPerPitcher = input("How many lemons in each pitcher? \n")
        return self.lemonsPerPitcher
        
    def add_sugar(self):
        self.sugarPerPitcher = input("How much sugar in each pitcher? \n")
        return self.sugarPerPitcher
        
    def add_ice(self):
        self.icePerCup = input("How many ice cubes in each cup? \n")
        return self.icePerCup
        
    def find_lemons_per_cup(self):
        self.lemonsPerCup = (Decimal(self.lemonsPerPitcher) / Decimal(10))
        return self.lemonsPerCup
        
    def find_sugar_per_cup(self):
        self.sugarPerCup = (Decimal(self.sugarPerPitcher) / Decimal(10))
        return self.sugarPerCup