from main import *

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
while (count < games):
    count += 1
    winner = playGame(players)
    if winner in list(winCount.keys()):
        winCount[winner] = winCount[winner] + 1
    else:
        winCount[winner] = 1

print(winCount)
