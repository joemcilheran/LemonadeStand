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
    
        weather = Weather.Weather()
        recipe = Recipe.Recipe()
        customerCounter = 0
        dailyServed = 0
        dailySatisfied = 0
        price = self.set_price()
        potentialCustomers = find_potential_customers(weather)
        
    def run_day(self):     
        week.display_day()
        self.weather.get_forecast()        
        bank.display_bankTotal()
        player.inventory.display_inventory()         
        week.player.purchase_items()        
        self.recipe.get_recipe()        
        self.set_price()                      
        self.find_potential_customers()
        print("counter " + str(customerCounter))
        self.run_all_customers()
        self.end_day()       
            
        
        
    def set_price(self):
        price = input("How much will you charge per cup of lemonade? \n")
        return price
        
    
    def find_potential_customers(self,weather):
        self.weather.get_temperature_factor()
        self.weather.get_weather_factor()
        potentialCustomers = (Decimal(200 + (temperatuerVariation) - (temperatureDifferential)) * Decimal(weatherFactor))        
        print(str(potentialCustomers) + "potentialCustomers")
        return potentialCustomers
        
    def run_all_customers(self):
        while counter < potentialCustomers:            
            self.add_to_customerCounter()
            print("counter " + str(customerCounter))
            customer = Customer.Customer()
            customer.run_customer()
        if inventory.sell_out_ice() == True:
            print("Sold Out!")
        if inventory.sell_out_other_items == True:
            print("Sold Out!")
            
    def add_to_dailySatisfied(self,customer):
        if customerSatisfaction == True:
            dailySatisfied = dailySatisfied + 1
        else:
            dailySatisfied = dailySatisfied
        return dailySatisfied
        
    def add_to_dailyServed(self):
        dailyServed = dailyServed + 1
        return dailyServed
        
    
    def end_day(self):
        week.add_to_satisfiedCustomers(week,day,bank)        
        week.add_to_servedCustomers(week,day)        
        week.find_popularity(week,day)
        print("You served " + str(dailyServed) + " customers out of " + str(potentialCustomers) + " potential customers.")
        print(str(dailySatisfied) + " of whom were satisfied.")
        print("You now have $" + str(bankTotal))
        print("and your popularity is " + str(popularity * 100) + " percent") 

    def add_to_customerCounter():
        customerCounter = customerCounter + 1
        return customerCounter
            