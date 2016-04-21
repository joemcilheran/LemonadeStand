import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Bank
import Recipe
import Week
from decimal import *
getcontext().prec = 4

class Player:

    def __init__(self):
    
        inventory = Inventory.Inventory()
        bank = Bank.Bank()
        cost = 0
        
        
    def purchase_cups(self):
        print("cups come in packages of 100 that cost 1 dollar")
        cost = input("How many cup packages would you like to purchase? \n")
        self.bank.withdraw(player)
        self.bank.display_bankTotal()
        self.inventory.get_cups(player)
        print(cost)
        return cost
        
    def purchase_lemons(self):
        print("Lemons come in cases of 10 that cost 1 dollar")
        cost = input("How many lemon cases would you like to purchase? \n")
        self.bank.withdraw(player)
        self.bank.display_bankTotal()        
        self.inventory.get_lemons(player)
        print(cost)
        return cost
        
    def purchase_sugar(self):
        print("Sugar comes in 10 cup bags that cost 1 dollar")
        cost = input("How many sugar bags would you like to purchase? \n")
        self.bank.withdraw(player)
        self.bank.display_bankTotal()        
        self.inventory.get_sugar(player)
        print(cost)
        return cost
        
    def purchase_ice(self):
        print("Ice comes in 150 cube bags that cost 1 dollar")
        cost = input("How many ice bags would you like to purchase? \n")
        self.bank.withdraw(player)
        self.bank.display_bankTotal()        
        self.inventory.get_ice(player)
        print(cost)
        return cost
        
    def purchase_items(self):
        self.purchase_cups()
        self.purchase_lemons()
        self.purchase_sugar()
        self.purchase_ice()
        
        