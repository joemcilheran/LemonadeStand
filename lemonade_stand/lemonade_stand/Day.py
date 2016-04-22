import random
import Weather
import Customer
import Chance
import Inventory
import Bank
import Recipe
from decimal import *
getcontext().prec = 4
import Week

class Day:

    def __init__(self):
    
        self.weather = Weather.Weather()
        self.recipe = Recipe.Recipe()
        self.customerCounter = 0
        self.dailyServed = 0
        self.dailySatisfied = 0
        self.price = 0
        self.potentialCustomers = 0
        
    def run_day(self,week):                                  
            self.find_potential_customers()
            print("counter " + str(self.customerCounter))
            self.run_all_customers(week,self)
                    
            
        
        
    def set_price(self):
        self.price = input("How much will you charge per cup of lemonade? \n")
        return self.price
        
    
    def find_potential_customers(self):
        self.weather.get_temperatureVariation()
        self.weather.get_temperatureDifferential()
        self.weather.get_weather_factor()
        self.potentialCustomers = int(round(Decimal(200 + (self.weather.temperatureVariation) - (self.weather.temperatureDifferential)) * Decimal(self.weather.weatherFactor)))        
        print(str(self.potentialCustomers) + "potentialCustomers")
        return self.potentialCustomers
        
    def run_all_customers(self,week,recipe):
        while self.customerCounter < self.potentialCustomers and week.inventory.sellOutIce == False and week.inventory.sellOutOtherItems == False:            
            self.add_to_customerCounter()
            print("counter " + str(self.customerCounter))
            self.customer = Customer.Customer()
            self.customer.run_customer(week,self)
            week.inventory.sell_out_ice(self)
            week.inventory.sell_out_other_items(self)
        if week.inventory.sellOutIce == True:
            print("Sold Out!")
        if week.inventory.sellOutOtherItems == True:
            print("Sold Out!")
            
    def add_to_dailySatisfied(self,customer):
        if self.customer.customerSatisfaction == True:
            self.dailySatisfied = self.dailySatisfied + 1
        else:
            self.dailySatisfied = self.dailySatisfied
        return self.dailySatisfied
        
    def add_to_dailyServed(self):
        self.dailyServed = self.dailyServed + 1
        return self.dailyServed
        
    
    
    def add_to_customerCounter(self):
        self.customerCounter = self.customerCounter + 1
        return self.customerCounter
        
    def end_day(self,week):
        week.add_to_satisfiedCustomers(self)        
        week.add_to_servedCustomers(self)        
        week.find_popularity()
        print("You served " + str(self.dailyServed) + " customers out of " + str(self.potentialCustomers) + " potential customers.")
        print(str(self.dailySatisfied) + " of whom were satisfied.")
        print("You now have $" + str(week.bank.bankTotal))
        print("and your popularity is " + str(week.popularity * 100) + " percent") 
        week.inventory.reset()
        input("Press Enter to continue")
        print("  ")
        print("  ")        
        print("  ")
        print("  ")
        
    def start_day(self,week):
        self.weather.get_weather()
        self.weather.get_temperature()        
        self.weather.get_forecast()                
        week.bank.display_bankTotal()
        week.inventory.display_inventory()         
        week.purchase_items()        
        self.recipe.get_recipe()        
        self.set_price()
        input("Press Enter to continue")        
            