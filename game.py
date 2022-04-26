from resources import housing, metallic_alloys, electronics
from transfer import Transfer
from countries import Countries
from time import sleep

class Player:

    def __init__(self, name):
        self.name = name
        
        
class Game:
    
#Randomly chose my country to be Carpania
    myCountry = "Carpania"
    initialStatePath = "initial_countries.xlsx"
    resourcePath = "Sample-Resources.xlsx"
    transform_resources = [housing, metallic_alloys, electronics] 
    countries = Countries(myCountry, transform_resources,
                              initialStatePath, resourcePath)   
   def play():     
        p1 = Player("Player")
        state = countries.getStateStatus()
        print("\nCountry Initial States")
        print("-----------------------\n")
        print(state)
        print("\nHello Player! This is the Trade & Transfer Game!")
        sleep(2)
        print("\nYour country will be Carpania!")
        sleep(2)
        print("\nCarpania's Resources (in millions):")
        print("Metallic Elements -> 100")
        print("Timber -> 300")
        print("Water -> 320")
        print("Housing -> 500")
        print("Metallic Alloys -> 500")
        print("Electronics -> 75")
        sleep(5)
        print("\nTime to Play!!!!")
        print("1. Trade Resources")
        print("2. Transform Resources")
        print("3. Exit")
        play = input("")
