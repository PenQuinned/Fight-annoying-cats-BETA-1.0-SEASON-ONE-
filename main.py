#imports
import time
import os
import random
#CatNames.txt
with open("catnames.txt", "r") as file:
    allText = file.read()
    randomCatName = list(map(str, allText.split()))
#variables
catb = "Cat with no name (error)"
powerb = 1
powera = 1
h = 100
eh = 100
opt = "sit and calmly wait"
working = 1
deathMessages = ["The bright light consumes you", "It was your time to go", "Aww man...", "The earth consumes you", "Such a sad passing...", "Wow, you got defeated soooo bad...", "lol you just died to a litteral house cat (:<", "remember the code: feline_1234xxxabcd"]
winamount = 0
loseamount = 0
messageToYou = ["I wish i could tell my mom i loved her, but you are ending me before i could ):", "I didn't mean to offend you! Please i take it ba-", "Remember when we were in kindergarden together, you were the bully. I thought you would have changed.", "I just want to say someth-", "*sobs* HELP ME!!!",  "remember the code: feline_1234xxxabcd"]
#lists

#hastag

#QGAMELOADER
print("QGAMELOADER")
print("V0.1")
time.sleep(1)
print("BOOTING GAME!")
time.sleep(1)
#MainGame

def tutorial():
    os.system("clear")
    print("Welcome to fight annoying cats, my name is boots!")
    time.sleep(3)
    print("Before you battle, you need to prove that your a cat.")
    time.sleep(3)
    os.system("clear")
    print(">entering cat quiz center<")
    time.sleep(3)
    os.system("clear")
    ##########
    ab = input("Meow (a), or woof (b)?")
    if ab == ("a"):
        print("Correct!")
    else:
        print("Excuse me? Get out of here!")
        time.sleep(3)
        tutorial()
    os.system("clear")
    ##########
    ab = input("Litter Box (a), or grass (b)?")
    if ab == ("a"):
        print("Correct!")
    else:
        print("Excuse me? Get out of here!")
        time.sleep(3)
        tutorial()
    os.system("clear")
    ##########
    ab = input("Finally, Love human (a), or scratch human (b)?")
    if ab == ("b"):
        print("Correct!")
    else:
        print("Excuse me? Get out of here!")
        time.sleep(3)
        tutorial()
    os.system("clear")
    ##########
    print("Okay, you have proved to know what the right and wrong is, now lets try a battle!")
    time.sleep(3)
    os.system("clear")
    print(">entering arena 1<")
    os.system("clear")
    print("Okay so lets head over to the battlefield!")
    time.sleep(2)
    print("Hmmmm... oh! You can go battle Frisky over there!")
    os.system("clear")
    catb = "Frisky"
    print(">beginning battle<")
    time.sleep(3)
    os.system("clear")
    print("Okay so, you will get three choices: Attack, Block, Run, Ask Frisky for money, Or Twerk!")
    time.sleep(1)
    print("...")
    time.sleep(3)
    print("Okay the last two might not be true.")
    time.sleep(2)
    print("but ANYWAYS")
    time.sleep(1)
    print("lets...")
    time.sleep(3)
    print("Battle")
    time.sleep(2)
    os.system("clear")
    print("Beginning battle.")
    time.sleep(0.5)
    print("Beginning battle..")
    time.sleep(0.5)
    print("Beginning battle...")
    time.sleep(0.5)
    print("Beginning battle....")
    time.sleep(0.5)
    print("Beginning battle.....")
    time.sleep(0.5)
    os.system("clear")
    

tutorial()

def themysteryroom():
    os.system("clear")
    print("...")
    time.sleep(2)
    print("it's time you learn a lesson")
    time.sleep(5)
    print("follow me...")
    time.sleep(3)
    print("Your father once was a great fighter")
    time.sleep(3)
    print("I, I, i thought my father worked in an office?")
    time.sleep(3)
    print("Wait, I still have more to say.")
    time.sleep(3)
    print("Your father won every single game. No cat could beat him.")
    time.sleep(3)
    print("But when he and your mother had you, he wanted to take a break from fighting...")
    time.sleep(3)
    print("When he came back, there was a new figher coming around")
    time.sleep(3)
    print("They didn't think your father was good enough...")
    time.sleep(3)
    print("He got so mad, he ran away.")
    time.sleep(3)
    print("And never came back.")
    time.sleep(3)
    print("Eventually you got a new father")
    time.sleep(3)
    print("But your old ones rage is still in you")
    time.sleep(3)
    print("WHAT?")
    time.sleep(3)
    print("And guess what, rage has a chemical called catrageocin")
    time.sleep(3)
    print("That is very valuable...")
    time.sleep(3)
    print("I'm here to extract it...")
    time.sleep(3)
    print("Wait, wha-")
    time.sleep(1)
    os.system("clear")
    print("You wake up in a cell")
    time.sleep(3)
    print("No door, no window")    
    time.sleep(3)
    print("All you have is a litter box and a bowl of water")
    time.sleep(3)
    print("You think you will spend the rest of your life in that cell")
    time.sleep(3)
    print("Every day you get anger sucked out of you.")
    time.sleep(3)
    print("One day, you figure out a plan...")
    time.sleep(3)
    os.system("clear")
    print("A game by ImQuinn")
    time.sleep(3)
    print("THE END")
def battle():
    global opt 
    global eh
    global h
    global powera
    global powerb
    print("WELCOME TO THE BATTLE!")
    print("THIS BATTLE IS:")
    print(f"You Vs: {catb}")
    print(f"{catb} has {powerb} power")
    print("Let the battle commence!")
    while working == 1:
        opt = input("(1) Attack, (2) Block, (3) run")
        if opt == "1":
            eh -= random.randint(5, 20)
            if powera >= 5:
                eh -5
            h -= random.randint(5, 20)
            if powerb >= 5:
                h -5
            print(f"You attacked. Your health is now {h},{catb} now has {eh} health!")
            time.sleep(5)
            os.system("clear")
        if opt == "2":
            eh += random.ranint(0, 5)
            h += random.ranint(0, 5)
            if powerb >= 5:
                eh += (5)      
            if powera >= 5:
                h += (5)
            print(f"You blocked. Your health is now {h}, {catb} now has {eh} health!")
            time.sleep(5)
            os.system("clear")
        if opt == "3":
            print("You run...")
            print("You find a place to rest...")
            h += random.randint(0, 5)
            if powera >= 5:
                h += 3
            print(f"You run. Huh, guess you were a widdle scared... but ANYWAYS... you now have {h} health, and {catb} has {eh} health")
            time.sleep(5)
            os.system("clear")
        if opt == "feline_1234xxxabcd":
            themysteryroom()
        if h <= 0:
            print(random(deathMessages))
            time.sleep(2)
            print("(you died)")
            time.sleep(3)
            os.system("clear")
            powerb += (1)
        if eh <= 0:
            print(f"one last message from {catb}:")
            time.sleep(3)
            print(random(messageToYou))
            time.sleep(3)
            print("*dies*")
            time.sleep(3)
            powera += 1
            
            
def battlecenter():
    global catb
    global powera
    os.system("clear")
    print("Welcome back to the battle center!")
    print(f"Your current level is: {powera}")
    time.sleep(3)
    print("Your next battle is in 15 seconds!")
    time.sleep(15)
    catb = random.choice(randomCatName)
    powerb = powera = (random.randint(0, 1))
    if powera <= 0:
        powera = 1
    if powerb <= 0:
        powerb = 2
    
        
    battle()
while working == 1:
    battlecenter()

    
