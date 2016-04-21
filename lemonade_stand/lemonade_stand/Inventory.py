import random
import Day
import Weather
import Customer
import Chance
import Bank
import Recipe
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
        
    def get_lemons(self,player):
        lemons = (int(cost) * 10)
        LemonTotal = (lemonTotal + lemons)
        return LemonTotal
        
    def get_sugar(self,player):
        sugar = (int(cost) * 10)
        SugarTotal = (sugarTotal + sugar)
        return SugarTotal
        
    def get_cups(self,player):
        cups = (int(cost) * 100)
        CupTotal = (cupTotal + cups)
        return CupTotal
    
    def get_ice(self,player):
        ice = (int(cost) * 150)
        IceTotal = (iceTotal + ice)
        return IceTotal    
        
        
    def adjust_lemons_from_purchase(self,recipe):
        lemonTotal = (Decimal(lemonTotal) - Decimal(lemonsPerCup))  
        return lemonTotal   
        
    def adjust_sugar_from_purchase(self,recipe):
        sugarTotal = (Decimal(sugarTotal) - Decimal(sugarPerCup))
        return sugarTotal
        
    def adjust_cups_from_purchase(self,recipe):
        cupTotal = (cupTotal - 1)
        return cupTotal
        
    def adjust_ice_from_purchase(self,recipe):
        iceTotal = (int(iceTotal) - int(icePerCup))
        return iceTotal
        
    def adjust_inventory(self):
        self.adjust_lemons_from_purchase(recipe)
        self.adjust_sugar_from_purchase(recipe)
        self.adjust_cups_from_purchase(recipe)
        self.adjust_ice_from_purchase(recipe)
        
    def sell_out_ice(self,recipe):
        if icePerCup != 0 and iceTotal < icePerCup:
           return True
        else: 
           return False
           
    def sell_out_other_items(self,recipe):
        if lemonTotal < lemonsPerCup or sugarTotal < sugarPerCup or cupTotal == 0:
            return True
        else: 
            return False