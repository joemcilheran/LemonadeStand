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
import Week

class Customer:

    def __init__(self):
        
        self.chance = Chance.Chance()
        self.chanceOfBuying = 0
        self.customerSatisfaction = 0
        self.tasteSatisfaction = 0
        self.strenghthSatisfaction = 0
        self.temperatureSatisfaction = 0
    
    def find_chance_of_buying(self,week,day):
        day.weather.get_weather_factor()
        day.weather.get_temperature_factor()
        if int(week.popularity) == 0:
            impulse = ((Decimal(day.weather.weatherFactor) * Decimal(day.weather.temperatureFactor)) * Decimal(100)) + 50 - Decimal(day.price)
        else:
            impulse = ((Decimal(day.weather.weatherFactor) * Decimal(day.weather.temperatureFactor) * Decimal(week.popularity)) * Decimal(100)) + 50 - Decimal(day.price)
       
        if impulse >= 75:
            self.chanceOfBuying = True
            return self.chanceOfBuying
        elif impulse < 75 and impulse > 35:
            self.chanceOfBuying = self.chance.get_fifty_percent_chance()
            return self.chanceOfBuying
        elif impulse <36 and impulse > 5:
            self.chanceOfBuying = self.chance.get_twenty_five_percent_chance()
            return self.chanceOfBuying
        else:
            self.chanceOfBuying = False
            return self.chanceOfBuying
            
    def find_customer_satisfaction(self,day):
        tastsat = self.find_taste_satisfaction(day)
        strengthsat = self.find_strength_satisfaction(day)
        tempsat = self.find_temperature_satisfaction(day)  
        satisfactionSet = (tastsat,strengthsat,tempsat)        
        if satisfactionSet.count(True) > 1:
            self.customerSatisfaction = True
            return self.customerSatisfaction
        else:
            self.customerSatisfaction = False
            return self.customerSatisfaction
        
        
        
    def find_taste_satisfaction(self,day):
        taste = abs(int(day.recipe.lemonsPerPitcher) - int(day.recipe.sugarPerPitcher))
        if taste == 0:
            self.tasteSatisfaction = self.chance.get_seventy_five_percent_chance()
            return self.tasteSatisfaction
        elif taste == 1:
            self.tasteSatisfaction = self.chance.get_fifty_percent_chance()
            return self.tasteSatisfaction
        elif taste == 2:
            self.tasteSatisfaction = self.chance.get_twenty_five_percent_chance()
            return self.tasteSatisfaction
        else:
            self.tasteSatisfaction = False
            return self.tasteSatisfaction
            
    def find_strength_satisfaction(self,day):
        strenghth = (int(day.recipe.lemonsPerPitcher) + int(day.recipe.sugarPerPitcher))
        if strenghth == 8:
            self.strenghthSatisfaction = self.chance.get_seventy_five_percent_chance()
            return self.strenghthSatisfaction
        elif strenghth == 9 or strenghth == 7:
            self.strenghthSatisfaction = self.chance.get_fifty_percent_chance()
            return self.strenghthSatisfaction
        elif strenghth == 10 or strenghth == 6:
            self.strenghthSatisfaction = self.chance.get_twenty_five_percent_chance()
            return self.strenghthSatisfaction
        else:
            self.strenghthSatisfaction = False
            return self.strenghthSatisfaction
            
    def find_temperature_satisfaction(self,day):
        day.weather.temperatureForecast = int(day.weather.temperatureForecast)
        day.recipe.icePerCup = int(day.recipe.icePerCup)
        if day.weather.temperatureForecast < 70:
            if day.recipe.icePerCup < 2:
                self.temperatureSatisfaction = self.chance.get_seventy_five_percent_chance()
                return self.temperatureSatisfaction
            elif day.recipe.icePerCup < 4:
                self.temperatureSatisfaction = self.chance.get_fifty_percent_chance()
                return self.temperatureSatisfaction
            else:
                self.temperatureSatisfaction = False
                return self.temperatureSatisfaction
                
        elif day.weather.temperatureForecast >= 70 and day.weather.temperatureForecast < 90:
            if day.recipe.icePerCup < 2:
               self.temperatureSatisfaction = self.chance.get_twenty_five_percent_chance()
               return self.temperatureSatisfaction
            elif day.recipe.icePerCup < 4:
               self.temperatureSatisfaction = self.chance.get_seventy_five_percent_chance()
               return self.temperatureSatisfaction
            elif day.recipe.icePerCup == 4:
               self.temperatureSatisfaction = self.chance.get_twenty_five_percent_chance()
               return self.temperatureSatisfaction
            else:
               self.temperatureSatisfaction = False
               return self.temperatureSatisfaction
               
        else:
            if day.recipe.icePerCup < 3:
               self.temperatureSatisfaction = self.chance.get_twenty_five_percent_chance()
               return self.temperatureSatisfaction
            elif day.recipe.icePerCup == 3:
               self.temperatureSatisfaction = self.chance.get_fifty_percent_chance()
               return self.temperatureSatisfaction
            else:
               self.temperatureSatisfaction = False
               return self.temperatureSatisfaction
               
    def run_customer(self, week,day):
        self.find_chance_of_buying(week,day)
        if self.chanceOfBuying == True:                
            week.bank.deposit(day)
            day.add_to_dailyServed()
            week.inventory.adjust_inventory(day)
            self.find_customer_satisfaction(day)
            day.add_to_dailySatisfied(day) 
        
        
                       
        
    
            
        
    