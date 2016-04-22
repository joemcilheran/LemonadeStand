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
    
        self.lemonTotal = 0
        self.sugarTotal = 0
        self.iceTotal = 0
        self.cupTotal = 0
        self.sellOutIce = 0
        self.sellOutOtherItems = 0
    
    def display_inventory(self):
        print("Inventory:")
        print(str(self.lemonTotal) + " lemons")
        print(str(self.sugarTotal) + " cups of sugar")
        print(str(self.iceTotal) + " cubes of ice")
        print(str(self.cupTotal) + " cups")
        
    def get_lemons(self,week):
        lemons = (int(week.cost) * 10)
        self.lemonTotal = (self.lemonTotal + lemons)
        return self.lemonTotal
        
    def get_sugar(self,week):
        sugar = (int(week.cost) * 10)
        self.sugarTotal = (self.sugarTotal + sugar)
        return self.sugarTotal
        
    def get_cups(self,week):
        cups = (int(week.cost) * 100)
        self.cupTotal = (self.cupTotal + cups)
        return self.cupTotal
    
    def get_ice(self,week):
        ice = (int(week.cost) * 150)
        self.iceTotal = (self.iceTotal + ice)
        return self.iceTotal    
        
        
    def adjust_lemons_from_purchase(self,day):
        self.lemonTotal = (Decimal(self.lemonTotal) - Decimal(day.recipe.lemonsPerCup))  
        return self.lemonTotal   
        
    def adjust_sugar_from_purchase(self,day):
        self.sugarTotal = (Decimal(self.sugarTotal) - Decimal(day.recipe.sugarPerCup))
        return self.sugarTotal
        
    def adjust_cups_from_purchase(self):
        self.cupTotal = (self.cupTotal - 1)
        return self.cupTotal
        
    def adjust_ice_from_purchase(self,day):
        self.iceTotal = (int(self.iceTotal) - int(day.recipe.icePerCup))
        return self.iceTotal
        
    def adjust_inventory(self,day):
        self.adjust_lemons_from_purchase(day)
        self.adjust_sugar_from_purchase(day)
        self.adjust_cups_from_purchase()
        self.adjust_ice_from_purchase(day)
        
    def sell_out_ice(self,day):
        if int(day.recipe.icePerCup) != 0 and int(self.iceTotal) < int(day.recipe.icePerCup):
           self.sellOutIce = True
           return self.sellOutIce
        else:
           self.sellOutIce = False
           return self.sellOutIce
           
    def sell_out_other_items(self,day):
        if Decimal(self.lemonTotal) < Decimal(day.recipe.lemonsPerCup) or Decimal(self.sugarTotal) < Decimal(day.recipe.sugarPerCup) or Decimal(self.cupTotal) == 0:
            self.sellOutOtherItems = True
            return self.sellOutOtherItems
        else: 
            self.sellOutOtherItems = False
            return self.sellOutOtherItems
            
    def melt_ice(self):
        self.iceTotal = 0
        return self.iceTotal
        
    def reset_sell_out_ice(self):
        self.sellOutIce = False
        return self.sellOutIce
        
    def reset_sell_out_other_items(self):
        self.sellOutOtherItems = False
        return self.sellOutOtherItems
        
    def reset(self):
        self.melt_ice()
        self.reset_sell_out_ice()
        self.reset_sell_out_other_items()
        