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
    
        lemonsPerPitcher = self.add_lemons()
        sugarPerPitcher = self.add_sugar()
        icePerCup = self.add_ice()
        lemonsPerCup = self.find_lemons_per_cup()
        sugarPerCup = self.find_sugar_per_cup()
        
    
    def get_recipe(self):
        recipe.add_lemons()
        recipe.add_sugar()
        recipe.add_ice()
        recipe.find_lemons_per_cup()
        recipe.find_sugar_per_cup()
    
    def add_lemons(self):
        lemonsPerPitcher = input("How many lemons in each pitcher? \n")
        return lemonsPerPitcher
        
    def add_sugar(self):
        sugarPerPitcher = input("How much sugar in each pitcher? \n")
        return sugarPerPitcher
        
    def add_ice(self):
        icePerCup = input("How many ice cubes in each cup? \n")
        return icePerCup
        
    def find_lemons_per_cup(self):
        lemonsPerCup = (Decimal(lemonsPerPitcher) / Decimal(10))
        return lemonsPerCup
        
    def find_sugar_per_cup(self):
        sugarPerCup = (Decimal(sugarPerPitcher) / Decimal(10))
        return sugarPerCup