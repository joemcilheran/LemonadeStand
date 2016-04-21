import random
import Day
import Customer
import Chance
import Inventory
import Bank
import Recipe
import Purchases
from decimal import *
getcontext().prec = 4
import Week

class Weather:

    def __init__(self):
        
        weatherForcast = weatherForcast
        temperatureForecast = temperatureForecast
    
    
    def get_weather(self):
        weatherList = ("Sunny", "Hazy", "Cloudy", "Rainy")
        weatherForecast = random.choice(weatherList)
        return weatherForecast
        print(weatherForecast)
        
    def get_temperature(self):
        temperatureForecast = random.randint(50,100)
        return temperatureForecast
        
    def get_weather_factor(self):
               
        if weatherForecast == "Sunny":
            return 1.00 
        elif weatherForecast == "Hazy":
            return 0.75
        elif weatherForecast == "Cloudy":
            return 0.50
        else:
            return 0.25
        
        
    def get_temperature_factor(self,temperature):
        temperatureFactor = Decimal(temperature) / Decimal(100)
        print("temperatureFactor" + str(temperatureFactor))
        return temperatureFactor
        
    
    
 