import sys
import random
import Day
import Weather
import Customer
import Chance
import Inventory
import Bank
import Recipe
import Week
from decimal import *
getcontext().prec = 4

class PlayGame:

    def __init__(self):
    
        self.week = Week.Week()
       
        
if __name__ == "__main__":
    gamePlay = PlayGame()
    gamePlay.week.run_week()