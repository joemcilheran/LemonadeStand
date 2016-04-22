import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Bank
import Recipe
from decimal import *
getcontext().prec = 4

class Week:

    def __init__(self):
        
        self.bank = Bank.Bank()
        self.inventory = Inventory.Inventory()
        self.dayCounter = 0
        self.servedCustomers = 0
        self.satisfiedCustomers = 0
        self.popularity = 0
        self.cost = 0
   
    def run_week(self):  
        self.dayCounter = 0
        while self.dayCounter < 7:
            self.add_to_dayCounter()
            self.display_day()
            day = Day.Day()
            day.weather.get_weather()
            day.weather.get_temperature()        
            day.weather.get_forecast()                
            self.bank.display_bankTotal()
            self.inventory.display_inventory()         
            self.purchase_items()        
            day.recipe.get_recipe()        
            day.set_price()
            self.inventory.display_inventory()
            day.run_day(self)
            self.end_day(day)
            
            
                   
    def find_popularity(self):
        if self.servedCustomers == 0:
            self.popularity = self.popularity
        else:
            self.popularity = Decimal(self.satisfiedCustomers) / Decimal(self.servedCustomers)
        print(self.popularity)
        return self.popularity
        
    def add_to_servedCustomers(self,day):
        self.servedCustomers = (self.servedCustomers + day.dailyServed)
        print(str(self.servedCustomers) + "servedCustomers")
        return self.servedCustomers
        
    def add_to_satisfiedCustomers(self,day):
        self.satisfiedCustomers = (self.satisfiedCustomers + day.dailySatisfied)
        print(str(self.satisfiedCustomers) + "satisfiedCustomers")
        return self.satisfiedCustomers
        
    def add_to_dayCounter(self):
        self.dayCounter = self.dayCounter + 1
        return self.dayCounter
        
    def display_day(self):
        print("Day " + str(self.dayCounter))
        
    def purchase_cups(self):
        print("cups come in packages of 100 that cost 1 dollar")
        self.cost = input("How many cup packages would you like to purchase? \n")
        self.bank.withdraw(self)
        self.bank.display_bankTotal()
        self.inventory.get_cups(self)
        print(self.cost)
        return self.cost
        
    def purchase_lemons(self):
        print("Lemons come in cases of 10 that cost 1 dollar")
        self.cost = input("How many lemon cases would you like to purchase? \n")
        self.bank.withdraw(self)
        self.bank.display_bankTotal()        
        self.inventory.get_lemons(self)
        print(self.cost)
        return self.cost
        
    def purchase_sugar(self):
        print("Sugar comes in 10 cup bags that cost 1 dollar")
        self.cost = input("How many sugar bags would you like to purchase? \n")
        self.bank.withdraw(self)
        self.bank.display_bankTotal()        
        self.inventory.get_sugar(self)
        print(self.cost)
        return self.cost
        
    def purchase_ice(self):
        print("Ice comes in 150 cube bags that cost 1 dollar")
        self.cost = input("How many ice bags would you like to purchase? \n")
        self.bank.withdraw(self)
        self.bank.display_bankTotal()        
        self.inventory.get_ice(self)
        print(self.cost)
        return self.cost
        
    def purchase_items(self):
        self.purchase_cups()
        self.purchase_lemons()
        self.purchase_sugar()
        self.purchase_ice()
        
    def end_day(self,day):
        self.add_to_satisfiedCustomers(day)        
        self.add_to_servedCustomers(day)        
        self.find_popularity()
        print("You served " + str(day.dailyServed) + " customers out of " + str(day.potentialCustomers) + " potential customers.")
        print(str(day.dailySatisfied) + " of whom were satisfied.")
        print("You now have $" + str(self.bank.bankTotal))
        print("and your popularity is " + str(self.popularity * 100) + " percent") 
        self.inventory.reset()
        
    def start_day(self):
        day.weather.get_weather()
        day.weather.get_temperature()        
        day.weather.get_forecast()                
        self.bank.display_bankTotal()
        self.inventory.display_inventory()         
        self.purchase_items()        
        day.recipe.get_recipe()        
        day.set_price()    
        

          