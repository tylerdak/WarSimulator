from main import *

import math, os, sys, time

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def getPlayerCount():
    print("Number of players: ", end="")
    playerCount = input()
    if (not (isInt(playerCount)) or int(playerCount) < 2):
        if (not isInt(playerCount)):
            print("Please enter a valid integer of at least 2.")
            return getPlayerCount()
        elif int(playerCount) == 1:
            print("Ah, a lonely game, I see.")
            print("You win by default!")
            print("Congratulations!")
        elif int(playerCount) == 0:
            print("No one showed up so I guess I win!")
        elif int(playerCount) < 0:
            print("Hmmm, negative players? Odd...")

    else:
        return int(playerCount)

def getNumOfGames():
    print("Number of games: ", end="")
    gameCount = input()
    if (not (isInt(gameCount)) or int(gameCount) < 1):
        if (not isInt(gameCount)):
            print("Please enter a valid integer of at least 1.")
            return getNumOfGames()

        elif int(gameCount) == 0:
            print("No game, no shame! But now nothing happens...")
            sys.exit()
        elif int(gameCount) < 0:
            print("I really don't know how to do that...\nSorry.")

    else:
        return int(gameCount)

print("Welcome to WAR")
games = getNumOfGames()
players = getPlayerCount()

if (players == None) or (games == None):
    sys.exit()

count = 0
winCount = {}

startTime = time.time()
lastcheckpoint = -1

while (count < games):
    count += 1
    with HiddenPrints():
        winner = playGame(players)
    if winner in list(winCount.keys()):
        winCount[winner] = winCount[winner] + 1
    else:
        winCount[winner] = 1
    percentDone = max(round(((count / games) * 100), 2), 0.01)
    currentDuration = time.time() - startTime
    expectedRemaining = round(((currentDuration * 100) / percentDone) - currentDuration, 0)
    if currentDuration - lastcheckpoint > 0.4:
        lastcheckpoint = currentDuration
        print((str)(percentDone) + "% done\t\t-\t\tETA: " + (str)(expectedRemaining) + "s")

print(winCount)
