import time
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

class Week:

    def __init__(self):
        
        self.bank = Bank.Bank()
        self.inventory = Inventory.Inventory()
        self.dayCounter = 0
        self.servedCustomers = 0
        self.satisfiedCustomers = 0
        self.popularity = 0
        self.cost = 0
   
    def run_week(self):
        self.begin_week()    
        self.dayCounter = 0
        while self.dayCounter < 7:
            self.add_to_dayCounter()
            self.display_day()
            day = Day.Day()
            day.start_day(self)
            time.sleep(1)
            #self.inventory.display_inventory()
            day.run_day(self)
            day.end_day(self)
        if self.dayCounter == 7:            
           self.end_of_week()    
            
                   
    def find_popularity(self):
        if self.servedCustomers == 0:
            self.popularity = self.popularity
        else:
            self.popularity = Decimal(self.satisfiedCustomers) / Decimal(self.servedCustomers)
        print(self.popularity)
        return self.popularity
        
    def add_to_servedCustomers(self,day):
        self.servedCustomers = (self.servedCustomers + day.dailyServed)
        print(str(self.servedCustomers) + "servedCustomers")
        return self.servedCustomers
        
    def add_to_satisfiedCustomers(self,day):
        self.satisfiedCustomers = (self.satisfiedCustomers + day.dailySatisfied)
        print(str(self.satisfiedCustomers) + "satisfiedCustomers")
        return self.satisfiedCustomers
        
    def add_to_dayCounter(self):
        self.dayCounter = self.dayCounter + 1
        return self.dayCounter
        
    def display_day(self):
        print("Day " + str(self.dayCounter))
        
    def purchase_cups(self):
        print("cups come in packages of 100 that cost 1 dollar")
        self.cost = input("How many cup packages would you like to purchase? \n")
        self.bank.withdraw(self)
        self.bank.display_bankTotal()
        self.inventory.get_cups(self)
        print(self.cost)
        return self.cost
        
    def purchase_lemons(self):
        print("Lemons come in cases of 10 that cost 1 dollar")
        self.cost = input("How many lemon cases would you like to purchase? \n")
        self.bank.withdraw(self)
        self.bank.display_bankTotal()        
        self.inventory.get_lemons(self)
        print(self.cost)
        return self.cost
        
    def purchase_sugar(self):
        print("Sugar comes in 10 cup bags that cost 1 dollar")
        self.cost = input("How many sugar bags would you like to purchase? \n")
        self.bank.withdraw(self)
        self.bank.display_bankTotal()        
        self.inventory.get_sugar(self)
        print(self.cost)
        return self.cost
        
    def purchase_ice(self):
        print("Ice comes in 150 cube bags that cost 1 dollar")
        self.cost = input("How many ice bags would you like to purchase? \n")
        self.bank.withdraw(self)
        self.bank.display_bankTotal()        
        self.inventory.get_ice(self)
        print(self.cost)
        return self.cost
        
    def purchase_items(self):
        self.purchase_cups()
        self.purchase_lemons()
        self.purchase_sugar()
        self.purchase_ice()
        
    def end_of_week(self):
        if int(self.bank.bankTotal) > 20:
            self.win_game()
        elif int(self.bank.bankTotal) > 0:
            self.lose_game()
        else:
            self.run()
        
            
    def win_game(self):
        print("Congratulations: you've made a profit.")
        print("You have $" + str(self.bank.bankTotal))
        print("You've Win!")
        input("Press enter to exit.")
        
    def lose_game(self):
        print("Sadly, you failed to make a profit this week.")
        print("You have $" + str(self.bank.bankTotal))
        print("You've lost.")
        input("Press enter to exit.")
        
    def run(self):
        print("You've ended the week $" + str(abs(self.bank.bankTotal)) + " in debt!")
        print("Your payday loan is due, and collections is knocking on the door.")
        print("RUN!")
        time.sleep(10)
        
    def begin_week(self):
        print("Welcome to Lemonade Stand. You have 7 days to make a profit selling lemonade.")
        print("You will begin with $20 dollars in your bank.")
        print("You will be responsible for purchasing supplies.")
        print("You will also be responsible for making the lemonade recipe and setting the price.")
        print("Watch the Forecast! The weather will affect how many potential customers you have,")
        print("as well as their chance of buying, which will also be based on your popularity,")
        print("and that will be based on previous customers' satisfaction.")
        print("customers' satisfaction will be based on your recipe.")
        print("Good luck!")
        input("press Enter to continue")
        

          