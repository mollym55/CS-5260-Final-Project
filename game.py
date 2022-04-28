from resources import housing, metallic_alloys, electronics
from transfer import Transfer
from countries import Countries
from time import sleep

class Player:

    def __init__(self, name):
        self.name = name
        
        
class Game:
    
    def play():
        #Randomly chose my country to be Carpania
        #myCountry = "Carpania"
        initialStatePath = "initial_countries.xlsx"
        resourcePath = "Sample-Resources.xlsx"
        transform_resources = [housing, metallic_alloys, electronics] 
        countries = Countries(myCountry, transform_resources,
                                  initialStatePath, resourcePath)   
        metallic_Elements = 0
        timber = 0
        water = 0
        housing = 0
        metallic_Alloys = 0
        electronics = 0

        p1 = Player("Player")
        state = countries.getStateStatus()
        #print("\nCountry Initial States")
        #print("-----------------------\n")
        #print(state)
        print("\nHello Player! This is the Beware of the Wumpus Game!")
        sleep(2)
        print("\n")
        print("     ------------      ")
        print("    /  @    @    \     ")
        print("   /      v       \    ")
        print("  /      BOO       \   ")
        print(" /                  \  ")
        print(" \                  /  ")
        print("  \/\/\/\/\/\/\/\/\/   ")
        print("\n")
        print("THE WUMPUS IS COMING FOR YOU!!!!")
        #print("\nYour country will be Carpania!")
        sleep(2)
        print("\nWhat country do you choose?")
        print("1. Atlantis")
        print("2. Brobdingnag")
        print("3. Carpania")
        print("4. Dinotopia")
        print("5. Erewhon")
        choose_Country = input("")
        if choose_Country == 1:
            myCountry = "Atlantis"
            print("\nYour country will be " + myCountry)
            metallic_Elements = 700
            timber = 2000
            water = 50
            housing = 100
            metallic_Alloys = 200
            electronics = 800
            print("\nYour Resources (in millions):")
            print("Metallic Elements -> " + metallic_Elements)
            print("Timber -> " + timber)
            print("Water -> " + water)
            print("Housing -> " + housing)
            print("Metallic Alloys -> " + metallic_Alloys)
            print("Electronics -> " + electronics)
        elif choose_Country == 2:
            myCountry = "Brobdingnag"
            print("\nYour country will be " + myCountry)
        elif choose_Country == 3:
            myCountry = "Carpania"
            print("\nYour country will be " + myCountry)
            
        elif choose_Country == 4:
            myCountry = "Dinotopia"
            print("\nYour country will be " + myCountry)
        elif choose_Country == 5:
            myCountry = "Erewhon"
            print("\nYour country will be " + myCountry)
        elif 
            exit()
        
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
        
    play()
    
    def exit():
        print("\nBye! Hope you had fun :)")
