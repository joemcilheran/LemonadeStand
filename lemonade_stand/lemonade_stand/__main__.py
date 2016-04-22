import sys
import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Bank
import Recipe
from Week import Week
from decimal import *
getcontext().prec = 4

class playgame():

    def __init__(self):
    
        self.week = Week()
       
        
if __name__ == "__main__":
    playgame = playgame()
    playgame.week.run_week()