import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Bank
import Purchases
from decimal import *
getcontext().prec = 4
import Week

class Recipe:

    def __init__(self):
        pass
    
    def get_recipe(self):
        lemonsPerPitcher = recipe.add_lemons()
        sugarPerPitcher = recipe.add_sugar()
        icePerCup = recipe.add_ice()
        lemonsPerCup = recipe.find_lemons_per_cup(lemonsPerPitcher)
        sugarPerCup = recipe.find_sugar_per_cup(sugarPerPitcher)
    
    def add_lemons(self):
        lemonsPerPitcher = input("How many lemons in each pitcher? \n")
        return lemonsPerPitcher
        
    def add_sugar(self):
        sugarPerPitcher = input("How much sugar in each pitcher? \n")
        return sugarPerPitcher
        
    def add_ice(self):
        icePerCup = input("How many ice cubes in each cup? \n")
        return icePerCup
        
    def find_lemons_per_cup(self,lemonsPerPitcher):
        lemonsPerCup = (Decimal(lemonsPerPitcher) / Decimal(10))
        return lemonsPerCup
        
    def find_sugar_per_cup(self,sugarPerPitcher):
        sugarPerCup = (Decimal(sugarPerPitcher) / Decimal(10))
        return sugarPerCup