import math 
import random


#    def __init__(self, name, players, score):
#        self.name = name
#        self.players = players
#        self.score = 0

# select the type of tournament you want to run
tourneyType = input("What kind of tournament do you want to run: \n 1: 1v1 \n 2: 2v2 \n 3: 3v3 \n 4: 4v4 \n 5: 5v5 \n")
print("You selected: "+ tourneyType)

# collects input on how many players are in the tournament 
playersNum = int(input("How many players are in your tournament: "))

# takes how many players were given for this tournament and iterates to decide how many players are needed for the list
print("Insert the names of the players that will be attending the tournament: ")
playerNames = []

def entryList(playersNum, playerNames):
    incVar = 1
    for i in range(playersNum):
        element = input("Player "+str(incVar)+": ")
        incVar += 1
        playerNames.append(element)

# Tournament functions that build the tournament type //oneVO = one vs one... etc 
def oneVO(playersNum, playerNames):
    ovoBracket = []
    winner = []
    getWinner = []
    teams = []
    seed = playersNum
    for x in playerNames: 
        ovoBracket.append(playerNames)
   
    random.shuffle(ovoBracket)
    while len(winner) > 1:
        for i in range(0, len(ovoBracket), 2):
            teams = getWinner(ovoBracket[i], ovoBracket[i+1])    
            #winner.append(teams)
    print(teams)
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
    entryList(playersNum, playerNames)
    oneVO(playersNum, playerNames)
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
    

