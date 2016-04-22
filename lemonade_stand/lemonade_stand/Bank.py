import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Recipe
from decimal import *
getcontext().prec = 4
import Week
class Bank:

    def __init__(self):
    
        self.bankTotal = 20
    
    
    def withdraw(self,week):
        self.bankTotal = (Decimal(self.bankTotal) - Decimal(week.cost))
        print(self.bankTotal)
        return Decimal(self.bankTotal)
        
    def deposit(self,day):
        self.bankTotal = (Decimal(self.bankTotal) + Decimal(Decimal(day.price) / Decimal(100)))
        print(self.bankTotal)
        return Decimal(self.bankTotal)
       
        
    def display_bankTotal(self):
        print("Bank total: $" + str(Decimal(self.bankTotal)))
