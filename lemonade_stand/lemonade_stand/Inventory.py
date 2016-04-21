import random
import Day
import Weather
import Customer
import Chance
import Bank
import Recipe
import Purchases
from decimal import *
getcontext().prec = 4
import Week

class Inventory:

    def __init__(self):
    
        lemonTotal = 0
        sugarTotal = 0
        iceTotal = 0
        cupTotal = 0
    
    def display_inventory(self):
        print("Inventory:")
        print(str(lemonTotal) + " lemons")
        print(str(sugarTotal) + " cups of sugar")
        print(str(iceTotal) + " cubes of ice")
        print(str(cupTotal) + " cups")
        
    def get_lemons(self):
        LemonTotal = (lemonTotal + newLemons)
        return LemonTotal
        
    def get_sugar(self):
        SugarTotal = (sugarTotal + newSugar)
        return SugarTotal
        
    def get_cups(self,cups):
        CupTotal = (cupTotal + cups)
        return CupTotal
    
    def get_ice(self,ice):
        IceTotal = (iceTotal + ice)
        return IceTotal    
        
    def use_lemons(self,lemons):
        LemonTotal = (Decimal(lemonTotal) - Decimal(lemons))
        return LemonTotal
        
    def use_sugar(self,sugar):
        SugarTotal = (Decimal(sugarTotal) - Decimal(sugar))
        return SugarTotal
        
    def use_cups(self):
        CupTotal = (cupTotal - cupsUsed)
        return CupTotal
        
    def use_ice(self):
        IceTotal = (iceTotal - iceUsed)
        return IceTotal
        
    def adjust_lemons_from_purchase(self,recipe):
        lemonTotal = (Decimal(lemonTotal) - Decimal(lemonsPerCup))      
    def adjust_sugar_from_purchase(self,recipe):
        sugarTotal = (Decimal(sugarTotal) - Decimal(sugarPerCup))
    def adjust_cups_from_purchase(self,recipe):
        cupTotal = (cupTotal - 1)
    def adjust_ice_from_purchase(self,recipe):
        iceTotal = (int(iceTotal) - int(icePerCup))
        
    def adjust_inventory(self,recipe):
        adjust_lemons_from_purchase