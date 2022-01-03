import math 
import random

# select the type of tournament you want to run
tourneyType = input("What kind of tournament do you want to run: \n 1: 1v1 \n 2: 2v2 \n 3: 3v3 \n 4: 4v4 \n 5: 5v5 \n")
print("You selected: "+ tourneyType)

# collects input on how many players are in the tournament 
playersNum = int(input("How many players are in your tournament: "))

# takes how many players were given for this tournament and iterates through a loop to decide how many players are needed for an array 
print("Insert the names of the players that will be attending the tournament: ")
PlayerNames = []
incVar = 1

for i in range(playersNum):
    element = input("Player "+str(incVar)+": ")
    incVar += 1
    PlayerNames.append(element)




# Tournament functions that build the tournament type //oneVT = one vs one... etc 
def oneVO():
    ovoBracket = []
    winner = []
    seed = playersNum
    for x in PlayerNames: 
        ovoBracket.append(PlayerNames)

    random.shuffle(ovoBracket)
    print(ovoBracket)             


    #result = ["",""]


def twoVT():
    print("fill")


def threeVT():
    print("fill")


def fourVF():
    print("fill")


def fiveVF():
    print("fill")


if tourneyType == '1':
    oneVO()
elif tourneyType == '2': 
    twoVT()
elif tourneyType == '3':
    threeVT()
elif tourneyType == '4':
    fourVF()
elif tourneyType == '5':
    fiveVF()  
else: 
    print("Yo buddy you didn't enter a valid number.")
    

