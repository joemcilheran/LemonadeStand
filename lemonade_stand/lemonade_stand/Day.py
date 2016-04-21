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
        dayCounter = dayCounter + 1
        
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
        
        while counter < potentialCustomers:
            
            counter = counter + 1
            print("counter " + str(counter))
            customer = Customer.Customer()
            buy = customer.find_chance_of_buying()
            print(buy)
            while buy == True:
                
            customer.buy_lemonade(dailyServed,bankTotal,price,lemonTotal,lemonsPerCup,sugarTotal,sugarPerCup,iceTotal,icePerCup,cupTotal)
                    
            customerSatisfaction = customer.find_customer_satisfaction(self,chance)
            dailySatisfied = self.add_to_dailySatisfied()
        if icePerCup != 0 and iceTotal == 0:
            print("Sold Out!")
        if lemonTotal == 0 or sugarTotal == 0 or cupTotal == 0:
            print("Sold Out!")
                
            satisfiedCustomers = (satisfiedCustomers + dailySatisfied)
            print(str(satisfiedCustomers) + "satisfiedCustomers")
            servedCustomers = (servedCustomers + dailyServed)
            print(str(servedCustomers) + "servedCustomers")
            popularity = self.find_popularity(satisfiedCustomers,servedCustomers,popularity)
            print("You served " + str(dailyServed) + " customers out of " + str(potentialCustomers) + " potential customers.")
            print(str(dailySatisfied) + " of whom were satisfied.")
            print("You now have $" + str(bankTotal))
            print("and your popularity is " + str(popularity * 100) + " percent")
        
        
    def set_price(self):
        price = input("How much will you charge per cup of lemonade? \n")
        return price
        
    
    def find_potential_customers(self):
        variation = random.randint(-10,10)
        print(str(variation) + "variation")
        temperatureDifferential = abs(temperatureForecast - 75)
        print(str(temperatureDifferential) + "temperatureDifferential")
        potentialCustomers = (Decimal(200 + (variation) - (temperatureDifferential)) * Decimal(weatherFactor))
        return int(potentialCustomers)
        
    def run_all_customers(self):
        while counter < potentialCustomers:            
            counter = counter + 1
            print("counter " + str(counter))
            customer = Customer.Customer()
            buy = customer.find_chance_of_buying()
            print(buy)
            while buy == True:                
                customer.buy_lemonade(self,inventory)                  
                customerSatisfaction = customer.find_customer_satisfaction(lemonsPerPitcher,sugarPerPitcher,icePerCup,tempForecast,chance)
                dailySatisfied = add_to_dailySatisfied()
        if icePerCup != 0 and iceTotal == 0:
            print("Sold Out!")
        if lemonTotal == 0 or sugarTotal == 0 or cupTotal == 0:
            print("Sold Out!")
            
    def add_to_dailySatisfied():
        if customerSatisfaction == True:
            dailySatisfied = dailySatisfied + 1
        else:
            dailySatisfied = dailySatisfied