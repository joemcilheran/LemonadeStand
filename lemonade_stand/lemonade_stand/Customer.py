import random
import Day
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

class Customer:

    def __init__(self):
        pass
    
    def find_chance_of_buying(self,weatherFactor,temperatureFactor,popularity,price,chance):
        if int(popularity) == 0:
            impulse = ((Decimal(weatherFactor) * Decimal(temperatureFactor)) * Decimal(100)) - Decimal(price)
        else:
            impulse = ((Decimal(weatherFactor) * Decimal(temperatureFactor) * Decimal(popularity)) * Decimal(100)) - Decimal(price)
       
        if impulse >= 75:
            return True
        elif impulse < 75 and impulse > 35:
            buy = chance.get_fifty_percent_chance()
            return buy
        elif impulse <36 and impulse > 5:
            buy = chance.get_twenty_five_percent_chance()
            return buy
        else:
            return False
            
    def find_customer_satisfaction(self,lemonsPerPitcher,sugarPerPitcher,icePerCup,tempForecast,chance):
        tastsat = self.find_taste_satisfaction(lemonsPerPitcher,sugarPerPitcher,chance)
        strensat = self.find_strength_satisfaction(lemonsPerPitcher,sugarPerPitcher,icePerCup,chance)
        tempsat = self.find_temperature_satisfaction(tempForecast,icePerCup,chance)
        satisfactionSet = (tastsat,strensat,tempsat)
        print(satisfactionSet)
        if satisfactionSet.count(True) > 1:
            return True
        else:
            return False
        
        
        
    def find_taste_satisfaction(self,lemonsPerPitcher,sugarPerPitcher,chance):
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
            return False
            
    def find_strength_satisfaction(self,lemonsPerPitcher,sugarPerPitcher,icePerCup,chance):
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
            return False
            
    def find_temperature_satisfaction(self,temperature,icePerCup,chance):
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
                return False
                
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
               return False
               
        else:
            if icePerCup < 3:
               temperatureSatisfaction = chance.get_twenty_five_percent_chance()
               return temperatureSatisfaction
            elif icePerCup == 3:
               temperatureSatisfaction = chance.get_fifty_percent_chance()
               return temperatureSatisfaction
            else:
               return True
               
    def buy_lemonade(self,dailyServed,bankTotal,price,lemonTotal,lemonsPerCup,sugarTotal,sugarPerCup,iceTotal,icePerCup,cupTotal):
        
        
        print(bankTotal)
        
        
        
                       
        
    
            
        
    