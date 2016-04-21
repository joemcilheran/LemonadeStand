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
        
        weatherForecast = self.get_weather()
        temperatureForecast = self.get_temperature()
        weatherFactor = self.get_weather_factor()
        temperatureFactor = self.get_temperature_factor()
        temperatureDifferential = self.get_temperatureDifferential()
        temperatureVariation = self.get_temperatureVariation()
    
    
    def get_weather(self):
        weatherList = ("Sunny", "Hazy", "Cloudy", "Rainy")
        weatherForecast = random.choice(weatherList)
        print(weatherForecast)
        return weatherForecast
        
    def get_temperature(self):
        temperatureForecast = random.randint(50,100)
        return temperatureForecast
       
        
    def get_weather_factor(self):
               
        if weatherForecast == "Sunny":
            weathFactor = 1.00 
        elif weatherForecast == "Hazy":
            weathFactor =  0.75
        elif weatherForecast == "Cloudy":
            weathFactor =  0.50
        else:
            weathFactor = 0.25
        print("weathFactor" + str(weatherFactor))
        return weatherForecast
        
        
    def get_temperature_factor(self):
        temperatureFactor = Decimal(temperature) / Decimal(100)
        return temperatureFactor
        print("temperatureFactor" + str(temperatureFactor))
        
        
    def get_forecast(self):
        self.get_weather()
        self.get_temperature()
        print("Forecast: " + str(temperatureForecast) + " degrees and " + weatherForecast)
    
    def get_temperatureVariation(self):
        temperatureVariation = random.randint(-10,10)
        return temperatureVariation
        print(str(temperatureVariation) + "variation")
        
    def get_temperatureDifferential(self):
        temperatureDifferential = abs(temperatureForecast - 75)
        return temperatureDifferential
        print(str(temperatureDifferential) + "temperatureDifferential")
 