from resources import housing, metallic_alloys, electronics
from transfer import Transfer
from countries import Countries
from time import sleep
import random
from goto import goto, comefrom, label

class Player:

    def __init__(self, name):
        self.name = name
        
        
class Game:
    
    def play():
        #Randomly chose my country to be Carpania
        myCountry = "Carpania"
        initialStatePath = "initial_countries.xlsx"
        resourcePath = "Sample-Resources.xlsx"
        transform_resources = [housing, metallic_alloys, electronics] 
        countries = Countries(myCountry, transform_resources,
                                  initialStatePath, resourcePath)   
        metallic_Elements = 0
        timber = 0
        water = 0
        housing_Value = 0
        metallic_Alloys = 0
        electronics_Value = 0
        min = 1
        max = 6
        dice_Value = 0

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
        choose_Country = int(input(""))
        if choose_Country == 1:
            myCountry = "Atlantis"
            print("\nYour country will be ", myCountry)
            metallic_Elements = 700
            timber = 2000
            water = 50
            housing_Value = 100
            metallic_Alloys = 200
            electronics_Value = 800
            print("\nYour Resources (in millions):")
            print("Metallic Elements -> ", metallic_Elements)
            print("Timber -> ", timber)
            print("Water -> ", water)
            print("Housing -> ", housing_Value)
            print("Metallic Alloys -> ", metallic_Alloys)
            print("Electronics -> ", electronics_Value)
        elif choose_Country == 2:
            myCountry = "Brobdingnag"
            print("\nYour country will be ", myCountry)
            metallic_Elements = 300
            timber = 1200
            water = 200
            housing_Value = 300
            metallic_Alloys = 200
            electronics_Value = 900
            print("\nYour Resources (in millions):")
            print("Metallic Elements -> ", metallic_Elements)
            print("Timber -> ", timber)
            print("Water -> ", water)
            print("Housing -> ", housing_Value)
            print("Metallic Alloys -> ", metallic_Alloys)
            print("Electronics -> ", electronics_Value)
        elif choose_Country == 3:
            myCountry = "Carpania"
            print("\nYour country will be ", myCountry)
            metallic_Elements = 100
            timber = 300
            water = 320
            housing_Value = 500
            metallic_Alloys = 500
            electronics_Value = 75
            print("\nYour Resources (in millions):")
            print("Metallic Elements -> ", metallic_Elements)
            print("Timber -> ", timber)
            print("Water -> ", water)
            print("Housing -> ", housing_Value)
            print("Metallic Alloys -> ", metallic_Alloys)
            print("Electronics -> ", electronics_Value)
            
        elif choose_Country == 4:
            myCountry = "Dinotopia"
            print("\nYour country will be ", myCountry)
            metallic_Elements = 200
            timber = 200
            water = 75
            housing_Value = 600
            metallic_Alloys = 75
            electronics_Value = 100
            print("\nYour Resources (in millions):")
            print("Metallic Elements -> ", metallic_Elements)
            print("Timber -> ", timber)
            print("Water -> ", water)
            print("Housing -> ", housing_Value)
            print("Metallic Alloys -> ", metallic_Alloys)
            print("Electronics -> ", electronics_Value)
            
        elif choose_Country == 5:
            myCountry = "Erewhon"
            print("\nYour country will be ", myCountry)
            metallic_Elements = 500
            timber = 1700
            water = 30
            housing_Value = 150
            metallic_Alloys = 40
            electronics_Value = 300
            print("\nYour Resources (in millions):")
            print("Metallic Elements -> ", metallic_Elements)
            print("Timber -> ", timber)
            print("Water -> ", water)
            print("Housing -> ", housing_Value)
            print("Metallic Alloys -> ", metallic_Alloys)
            print("Electronics -> ", electronics_Value)
            
        else:
            exit()
        
        sleep(5)
        print("\nTime to Play!!!! Roll the dice!")
        sleep(2)
        dice_Value = random.randint(min, max)
        print("\nYou rolled ", dice_Value)
        
        if dice_Value == 1:
            print("Yay! +500 to each resource")
            metallic_Elements += 500
            timber += 500
            water += 500
            housing_Value += 500
            metallic_Alloys += 500
            electronics_Value += 500
            print("\nYour Resources (in millions):")
            print("Metallic Elements -> ", metallic_Elements)
            print("Timber -> ", timber)
            print("Water -> ", water)
            print("Housing -> ", housing_Value)
            print("Metallic Alloys -> ", metallic_Alloys)
            print("Electronics -> ", electronics_Value)
        elif dice_Value == 2:
            print("Oh no! -200 to Timber")
            timber -= 200
            if timber <= 0:
                print("You don't have anymore timber. The Wumpus won!")
                exit()
        elif dice_Value == 3:
            print("You stepped in the Wumpus Dark Hole! You lose :(")
            exit()
        elif dice_Value == 4:
            print("Whoop Whoop! You defeated the Wumpus!")
            exit()
        elif dice_Value == 5:
            print("Boo, -300 to all resources")
            metallic_Elements -= 300
            timber -= 300
            water -= 300
            housing_Value -= 300
            metallic_Alloys -= 300
            electronics_Value -= 300
            if metallic_Elements <= 0:
                print("You don't have anymore metallic elements. The Wumpus won!")
                exit()
            if timber <= 0:
                print("You don't have anymore timber. The Wumpus won!")
                exit()
            if water <= 0:
                print("You don't have anymore water. The Wumpus won!")
                exit()
            if housing_Value <= 0:
                print("You don't have anymore housing. The Wumpus won!")
                exit()
            if metallic_Alloys <= 0:
                print("You don't have anymore metallic alloys. The Wumpus won!")
                exit()
            if electronics_Value <= 0:
                print("You don't have anymore electronics. The Wumpus won!")
                exit()
        elif dice_Value == 6:
            print("Free Pass!")
        
        print("\nWhat to roll again?")
        print("1. Yes")
        print("2. No, I'm bored lol")
        
       
        
        
    v = play()
    
    
    
    
        
    
        
        
