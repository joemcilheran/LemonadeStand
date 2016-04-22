import random
import Day
import Customer
import Chance
import Inventory
import Bank
import Recipe
from decimal import *
getcontext().prec = 4
import Week

class Weather:

    def __init__(self):
        
        self.weatherForecast = 0
        self.temperatureForecast = 0
        self.weatherFactor = 0
        self.temperatureFactor = 0
        self.temperatureDifferential = 0
        self.temperatureVariation = 0
    
    
    def get_weather(self):
        weatherList = ("Sunny", "Hazy", "Cloudy", "Rainy")
        self.weatherForecast = random.choice(weatherList)
        print("and " + self.weatherForecast)
        return self.weatherForecast
        
    def get_temperature(self):
        self.temperatureForecast = random.randint(50,100)
        print(str(self.temperatureForecast) + "degrees")
        return self.temperatureForecast
       
        
    def get_weather_factor(self):               
        if self.weatherForecast == "Sunny":
            self.weatherFactor = 1.00 
        elif self.weatherForecast == "Hazy":
            self.weatherFactor =  0.75
        elif self.weatherForecast == "Cloudy":
            self.weatherFactor =  0.50
        else:
            self.weatherFactor = 0.25
        print("weatherFactor" + str(self.weatherFactor))
        return self.weatherFactor
        
        
    def get_temperature_factor(self):
        self.temperatureFactor = Decimal(self.temperatureForecast) / Decimal(100)
        print("temperatureFactor" + str(self.temperatureFactor))
        return self.temperatureFactor
        
        
        
    def get_forecast(self):       
        print("Forecast: " + str(self.temperatureForecast) + " degrees and " + self.weatherForecast)
        
    
    def get_temperatureVariation(self):
        self.temperatureVariation = random.randint(-10,10)        
        print(str(self.temperatureVariation) + "variation")
        return self.temperatureVariation
        
    def get_temperatureDifferential(self):
        self.temperatureDifferential = abs(self.temperatureForecast - 75)
        print(str(self.temperatureDifferential) + "temperatureDifferential")
        return self.temperatureDifferential
        
 