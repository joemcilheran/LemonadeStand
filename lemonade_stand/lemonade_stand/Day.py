import random
import Weather
import Customer
import Chance
import Inventory
import Bank
import Recipe
import Purchases
from decimal import *
getcontext().prec = 4
import Week

class Day:

    def __init__(self):
    
        weather = Weather.Weather()
        recipe = Recipe.Recipe()
        counter = 0
        dailyServed = 0
        dailySatisfied = 0
        price = price
        
    def run_day(self,week):                
        print("Day " + str(dayCounter))        
        weatherForecast = self.weather.get_weather()
        temperatureForecast = self.weather.get_temperature()
        print("Forecast: " + str(temperatureForecast) + " degrees and " + weatherForecast)
        print("Bank total: $" + str(bankTotal))
        displayInventory = player.inventory.display_inventory()         
        purchaseItems = week.player.purchase_items()        
        getRecipe = self.recipe.get_recipe()        
        price = self.set_price()
        temperatureFactor = self.weather.get_temperature_factor()
        weatherFactor = self.weather.get_weather_factor()
        print("weathFactor" + str(weatherFactor))       
        potentialCustomers = self.find_potential_customers()
        print(str(potentialCustomers) + "potentialCustomers")        
        print("counter " + str(counter))
        allCustomers = self.run_all_customers()
        endOfDay =  self.end_day       
            
        
        
    def set_price(self):
        price = input("How much will you charge per cup of lemonade? \n")
        return price
        
    
    def find_potential_customers(self):
        temperatureVariation = random.randint(-10,10)
        print(str(tempVariation) + "variation")
        temperatureDifferential = abs(temperatureForecast - 75)
        print(str(temperatureDifferential) + "temperatureDifferential")
        potentialCustomers = (Decimal(200 + (variation) - (temperatureDifferential)) * Decimal(weatherFactor))
        return int(potentialCustomers)
        
    def run_all_customers(self):
        while counter < potentialCustomers:            
           oneCustomer = self.run_one_customer():
        if icePerCup != 0 and iceTotal < icePerCup:
            print("Sold Out!")
        if lemonTotal < lemonsPerCup or sugarTotal < sugarPerCup or cupTotal == 0:
            print("Sold Out!")
            
    def add_to_dailySatisfied(self):
        if customerSatisfaction == True:
            dailySatisfied = dailySatisfied + 1
        else:
            dailySatisfied = dailySatisfied
        return dailySatisfied
        
    def add_to_dailyServed(self):
        dailyServed = dailyServed + 1
        return dailyServed
        
    def run_one_customer(self,):
        counter = counter + 1
        print("counter " + str(counter))
        customer = Customer.Customer()
        chanceOfBuying = customer.find_chance_of_buying()
        print(chanceOfBuying)
        while chanceOfBuying == True:                
            bankTotal = bank.deposit(bank,day)
            dailyServed = self.add_to_dailyServed()
            adjustedInventory = inventory.adjust_inventory(inventory,recipe)
            customerSatisfaction = customer.find_customer_satisfaction(recipe,weather,chance)
            dailySatisfied = add_to_dailySatisfied() 
    
    def end_day():
        satisfiedCustomers = week.add_to_satisfiedCustomers(week,day)
        print(str(satisfiedCustomers) + "satisfiedCustomers")
        servedCustomers = week.add_to_servedCustomers(week,day)
        print(str(servedCustomers) + "servedCustomers")
        popularity = self.find_popularity(week,day)
        print("You served " + str(dailyServed) + " customers out of " + str(potentialCustomers) + " potential customers.")
        print(str(dailySatisfied) + " of whom were satisfied.")
        print("You now have $" + str(bankTotal))
        print("and your popularity is " + str(popularity * 100) + " percent")    