import random
import time
#Variabeln:
correctPathZwei = random.randint(1,2)
correctPath = random.randint(1,2)
playAgain = "y"

def startMenue():
    time.sleep(1)
    print("~~~~~~~~~~")
    print("Start Game")
    print("~~~~~~~~~~")
    time.sleep(2)
    print("~~~~~~~~~~~~~~~~~~")
    print("Escape the Dungeon")
    print("~~~~~~~~~~~~~~~~~~")
    time.sleep(2)
    print("you are trapped in a dungeon")
    time.sleep(2)
    print("there are two ways to try to get out,")
    time.sleep(2)
    print("but only one of them leads out the dungeon,")
    time.sleep(2)
    print("the other one will lead to your death!")
    print()


     
def choosePath():
    path = ""
    while path != "1" and path != "2":
        time.sleep(1)
        path = input("Which path will you choose? (1.right or 2.left)?: ")
    return str(path)
        

def checkPath(choosenPath):
    time.sleep(2)
    print("test")
    time.sleep(1)
    print("text")

    if choosenPath == str(correctPath):
        time.sleep(2)
        print("weg 2 true")
        time.sleep(1)
        print("test2")
            
    else:
        time.sleep(1)
        print("weg 2 false")    

def choosePathZwei():
    pathZwei = ""
    while pathZwei != "1" and pathZwei != "2": # input validation
        time.sleep(1)
        pathZwei = input("Which path will you choose? (1.right or 2.left): ")
    return pathZwei

def checkPathZwei(choosePathZwei,choosenPath):
    time.sleep(2)
    print("you run through the tunnel")
    print("......")
    time.sleep(2)
    print("you can feel a slight breeze of air,")
    time.sleep(2)
    print("a good sign...")
    print()
    time.sleep(2)
    print(choosePathZwei,str(correctPathZwei))
    
    if choosePathZwei == str(correctPathZwei) and choosenPath == str(correctPath):
        time.sleep(1)
        print("you already can see a ray of light...")
        time.sleep(1.5)
        print("you stepped out of the dungeon and breath the fresh air.")
        time.sleep(2)
        print("you have managed to escape the dungeon, Good Job!")
        time.sleep(2)
        print("~~~~~~~")
        print("THE END")
        print("~~~~~~~")        
        
    else:
        time.sleep(1)
        print("it is getting darker...")
        time.sleep(2)
        print("something is wrong here...")
        time.sleep(2)
        print("the siluets beguins to blurr.... ")
        time.sleep(2)
        print("you feel that you are falling ,but you can´t react... ")
        time.sleep(2)
        print("unconscious you fall on the cold floor.")
        time.sleep(1)
        print("You are dead")
        time.sleep(2)
        print("~~~~~~~")
        print("THE END")
        print("~~~~~~~")
        
while playAgain == "y":
        
    time.sleep(1)
    startMenue()
    print(correctPath)
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    time.sleep(1)
    print(correctPathZwei)
    choiceZwei = choosePathZwei()
    checkPathZwei(choiceZwei,choice)
    time.sleep(1)
    playAgain = input("Do you want to play again [y/n]?: ")

    if playAgain != "y":
        time.sleep(1)
        print("Thanks for playing!")
        time.sleep(0.5)
        print("Bye")
