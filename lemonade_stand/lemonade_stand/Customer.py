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
        
        chanceOfBuying = self.find_chance_of_buying(weather,week,price,chance)
        customerSatisfaction = self.find_customer_satisfaction()
        tasteSatisfaction = self.find_taste_satisfaction(recipe,chance)
        strenghthSatisfaction = self.find_strenghth_satisfaction(recipe,chance)
        temperatureSatisfaction = self.find_temperature_satisfaction(weather,recipe,chance)
        satisfactionSet = (tasteSatisfaction,strenghthSatisfaction,temperatureSatisfaction)
    
    def find_chance_of_buying(self,weather,week,price,chance):
        if int(popularity) == 0:
            impulse = ((Decimal(weatherFactor) * Decimal(temperatureFactor)) * Decimal(100)) - Decimal(price)
        else:
            impulse = ((Decimal(weatherFactor) * Decimal(temperatureFactor) * Decimal(popularity)) * Decimal(100)) - Decimal(price)
       
        if impulse >= 75:
            chanceOfBuying = True
            return chanceOfBuying
        elif impulse < 75 and impulse > 35:
            chanceOfBuying = chance.get_fifty_percent_chance()
            return chanceOfBuying
        elif impulse <36 and impulse > 5:
            chanceOfBuying = chance.get_twenty_five_percent_chance()
            return chanceOfBuying
        else:
            chanceOfBuying = False
            return chanceOfBuying
            
    def find_customer_satisfaction(self):
        self.find_taste_satisfaction(recipe,chance)
        self.find_strength_satisfaction(recipe,chance)
        self.find_temperature_satisfaction(weather,recipe,chance)       
        print(satisfactionSet)
        if satisfactionSet.count(True) > 1:
            customerSatisfaction = True
            return customerSatisfaction
        else:
            customerSatisfaction = False
            return customerSatisfaction
        
        
        
    def find_taste_satisfaction(self,recipe,chance):
        taste = abs(int(lemonsPerPitcher) - int(sugarPerPitcher))
        if taste == 0:
            tasteSatisfaction = chance.get_seventy_five_percent_chance()
            return tasteSatisfaction
        elif taste == 1:
            tasteSatisfaction = chance.get_fifty_percent_chance()
            return tasteSatisfaction
        elif taste == 2:
            tasteSatisfaction = chance.get_twenty_five_percent_chance()
            return tasteSatisfaction
        else:
            tasteSatisfaction = False
            return tasteSatisfaction
            
    def find_strength_satisfaction(self,recipe,chance):
        strenghth = (int(lemonsPerPitcher) + int(sugarPerPitcher))
        if strenghth == 8:
            strenghthSatisfaction = chance.get_seventy_five_percent_chance()
            return strenghthSatisfaction
        elif strenghth == 9 or strenghth == 7:
            strenghthSatisfaction = chance.get_fifty_percent_chance()
            return strenghthSatisfaction
        elif strenghth == 10 or strenghth == 6:
            strenghthSatisfaction = chance.get_twenty_five_percent_chance()
            return strenghthSatisfaction
        else:
            strenghthSatisfaction = False
            return strenghthSatisfaction
            
    def find_temperature_satisfaction(self,weather,recipe,chance):
        temperature = int(temperature)
        icePerCup = int(icePerCup)
        if temperature < 70:
            if icePerCup < 2:
                temperatureSatisfaction = chance.get_seventy_five_percent_chance()
                return temperatureSatisfaction
            elif icePerCup < 4:
                temperatureSatisfaction = chance.get_fifty_percent_chance()
                return temperatureSatisfaction
            else:
                temperatureSatisfaction = False
                return temperatureSatisfaction
                
        elif temperature >= 70 and temperature < 90:
            if icePerCup < 2:
               temperatureSatisfaction = chance.get_twenty_five_percent_chance()
               return temperatureSatisfaction
            elif icePerCup < 4:
               temperatureSatisfaction = chance.get_seventy_five_percent_chance()
               return temperatureSatisfaction
            elif icePerCup == 4:
               temperatureSatisfaction = chance.get_twenty_five_percent_chance()
               return temperatureSatisfaction
            else:
               temperatureSatisfaction = False
               return temperatureSatisfaction
               
        else:
            if icePerCup < 3:
               temperatureSatisfaction = chance.get_twenty_five_percent_chance()
               return temperatureSatisfaction
            elif icePerCup == 3:
               temperatureSatisfaction = chance.get_fifty_percent_chance()
               return temperatureSatisfaction
            else:
               temperatureSatisfaction = False
               return temperatureSatisfaction
               
    def run_customer(self):
        customer.find_chance_of_buying(weather,week,price,chance)
        print(chanceOfBuying)
        while chanceOfBuying == True:                
            bank.deposit(bank,day)
            day.add_to_dailyServed(day)
            inventory.adjust_inventory(inventory)
            self.find_customer_satisfaction(recipe,weather,chance)
            day.add_to_dailySatisfied(day) 
        
        
                       
        
    
            
        
    