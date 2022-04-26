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
        

    p1 = Player("Player")
    state = countries.getStateStatus()
    print("\nCountry Initial States")
    print("-----------------------\n")
    print(state)
    print("\nHello Player! This is the Trade & Transfer Game!")
    sleep(2)
    print("Your country will be Carpania")
