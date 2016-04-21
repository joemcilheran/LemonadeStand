import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Bank
import Recipe
import Week
import Purchases
from decimal import *
getcontext().prec = 4

class Player:

    def __init__(self):
    
        inventory = Inventory.Inventory()
        bank = Bank.Bank()
        
        
        
    def purchase_cups(self):
        print("cups come in packages of 100 that cost 1 dollar")
        cost = input("How many cup packages would you like to purchase? \n")
        bankTotal = self.bank.withdraw(bankTotal,cost)
        print("Bank total: $" + str(bankTotal))
        cups = (int(cost) * 100)
        cupTotal = self.inventory.get_cups(cupTotal,cups)
        
    def purchase_lemons(self):
        print("Lemons come in cases of 10 that cost 1 dollar")
        cost = input("How many lemon cases would you like to purchase? \n")
        bankTotal = self.bank.withdraw(bankTotal,cost)
        print("Bank total: $" + str(bankTotal))
        lemons = (int(cost) * 10)
        lemonTotal = self.inventory.get_lemons(lemonTotal,lemons) 
        
    def purchase_sugar(self):
        print("Sugar comes in 10 cup bags that cost 1 dollar")
        cost = input("How many sugar bags would you like to purchase? \n")
        bankTotal = self.bank.withdraw(bankTotal,cost)
        print("Bank total: $" + str(bankTotal))
        sugar = (int(cost) * 10)
        sugarTotal = self.inventory.get_sugar(sugarTotal,sugar)
        
    def purchase_ice(self):
        print("Ice comes in 150 cube bags that cost 1 dollar")
        cost = input("How many ice bags would you like to purchase? \n")
        bankTotal = self.bank.withdraw(bankTotal,cost)
        print("Bank total: $" + str(bankTotal))
        ice = (int(cost) * 150)
        iceTotal = self.inventory.get_ice(iceTotal,ice)
        
    def purchase_items(self):
        purchaseCups = self.purchase_cups()
        purchaseLemons = self.purchase_lemons()
        purchaseSugar = self.purchase_sugar()
        purchaseIce = self.purchase_ice()
        
        