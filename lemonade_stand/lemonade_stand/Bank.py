import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Recipe
import Purchases
from decimal import *
getcontext().prec = 4
import Week
class Bank:

    def __init__(self):
    
        bankTotal = 20
    
    
    def withdraw(self,bankTotal,cost):
        bankTotal = (Decimal(bankTotal) - Decimal(cost))
        return bankTotal
        
    def deposit(self,bankTotal,price):
        bankTotal = (Decimal(banktotal) + Decimal(Decimal(price) / Decimal(100)))
        print(bankTotal)
        return bankTotal
