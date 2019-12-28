from random import *
import sys
from isInt import isInt

def playGame(players):
    types = ["C","D","H","S"]
    numbers = ["2","3","4","5","6","7","8","9","10","11","12","13","14"]

    cards = []

    for type in types:
        for number in numbers:
            cards.append(type + "-" + number)




    playerCount = players



    print("Great! " + str(playerCount) + " players! Let's get the deck shuffled and dealt.")

    numCardsEach = int(len(cards)/playerCount)
    print("Dealing " + str(numCardsEach) + " cards to each player!")

    def dealCards():
        dict = {}
        shuffle(cards)

        #create the players and store them
        for i in range(playerCount):
            playerCards = [[],[]]
            player = "Player " + str(i + 1)
            dict[player] = playerCards

        lastPlayer = "Player " + str(playerCount)

        #give players cards
        for card in cards:
            lastPlayerNumber = int(lastPlayer[len(lastPlayer)-1]) #gets last letter
            if lastPlayerNumber == playerCount:
                lastPlayer = "Player 1"
            else:
                lastPlayer = "Player " + str(lastPlayerNumber + 1)

            currentCards = dict[lastPlayer][0]
            currentCards.append(card)
            dict[lastPlayer][0] = currentCards

        return dict


    allPlayerCards = dealCards()
    print("The cards have been dealt!")

    round = 0
    playersWithCards = list(allPlayerCards.keys())

    def doWar(winner, cardNumbers, cardsIn, playersPassed):
        # Handle two winners
        # 2.2.1 Find People in War
        playersInWar = []
        playersInWar.extend(playersPassed)
        warPeople = []
        # while (winner in cardNumbers):
        #     index = cardNumbers.index(winner)
        #
        #     # Only include a player if they have some card(s)
        #     if (len(allPlayerCards[(playersInWar)[index]][0]) > 0):
        #         cardNumbers.remove(cardNumbers[index])
        #         warPeople.append((playersInWar)[index])
        #         playersInWar.remove(playersInWar[index])
        #     else:
        #         victim = (cardNumbers)[index]
        #         del cardNumbers[index]
        #         # cardNumbers.append(victim)
        #         playersInWar.remove(playersInWar[index])


        for i in range(len(cardNumbers)):
            if cardNumbers[i] == winner:
                if len(allPlayerCards[playersInWar[i]][0]) > 0:
                    warPeople.append(playersInWar[i])

        print("warPeople = ", end ="")
        print(playersInWar)
        print(warPeople)

        if (len(warPeople) == 1):
            allPlayerCards[warPeople[0]][1].extend(cardsIn)

            return warPeople[0]
        elif (len(warPeople) == 0):
            winner = sample(playersPassed,1)[0]
            allPlayerCards[winner][1].extend(cardsIn)
            return winner

        # 2.2.2 If any people have < 4 in the [0], get the lowest len for the [0]s and do War with that number of cards
        wagingNumber = 4
        for person in warPeople:
            if (len(allPlayerCards[person][0]) < wagingNumber):
                print("Setting wage number...")
                wagingNumber = len(allPlayerCards[person][0])
            else:
                print("Not setting wage number: ")
                print("cards for person: ")
                print(allPlayerCards[person][0])

        # 2.2.3 Put the first few cards into the wagingPile
            # STEP 1: Get one card from each player
        cardPile = []
        comparePile = []
        for i in range(len(warPeople)):
            playerID = (warPeople)[i]
            for j in range(wagingNumber):
                if len(allPlayerCards[playerID][0]) < 1:
                    print("Sample larger than population!!")
                    print("Waging: " + str(wagingNumber))
                    print("j = " + str(j))
                thisCard = sample(allPlayerCards[playerID][0],1)[0]
                cardPile.append(thisCard)
                if j == (wagingNumber - 1): # this is the card to compare with the others
                    print("printing... " + str(j))
                    comparePile.append(thisCard)
                allPlayerCards[playerID][0].remove(thisCard)



        comparedNumbers = []
        for card in comparePile:
            comparedNumbers.append(int(card.split("-")[1]))

        # Get winning number
        winner = max(comparedNumbers)
        winningPlayer = ""

        if (cardNumbers.count(winner) > 1):
            cardPile.extend(cardsIn)
            return doWar(winner, comparedNumbers, cardPile, warPeople)

        else:
            # Get winning player
            index = comparedNumbers.index(winner)
            winningPlayer = (warPeople)[index]

            # give cardsIn + cardPile to winner
            cardPile.extend(cardsIn)
            allPlayerCards[winningPlayer][1].extend(cardPile)


            return winningPlayer

    def playRound(players):
        print("Starting Round " + str(round) + "!")
        print("Players in the game: " + str(len(playersWithCards)))

        # STEP 1: Get one card from each player
        cardsIn = []
        for i in range(len(playersWithCards)):
            playerID = (playersWithCards)[i]
            thisCard = sample(allPlayerCards[playerID][0],1)[0]
            cardsIn.append(thisCard)
            print(allPlayerCards[playerID][0])
            print(thisCard)
            allPlayerCards[playerID][0].remove(thisCard)

        # STEP 2: Compare cards
        # 2.1 Convert cards to values
        cardNumbers = []
        for card in cardsIn:
            cardNumbers.append(int(card.split("-")[1]))

        # Get winning number
        winner = max(cardNumbers)
        winningPlayer = ""

        if (cardNumbers.count(winner) > 1):
            # doWar will handle the winnings
            winningPlayer = doWar(winner, cardNumbers, cardsIn, (playersWithCards))

        else:
            # Get winning player
            index = cardNumbers.index(winner)
            winningPlayer = (playersWithCards)[index]

            #handle winnings
            allPlayerCards[winningPlayer][1].extend(cardsIn)

        # STEP 4 & 5: Move [1] to [0] if a player's [0] is empty but the [1] is not
        #             Eliminate players with no cards
        playersToRemove = []

        for person in playersWithCards:
            print(person)
            print(allPlayerCards[person][0])
            if len(allPlayerCards[person][0]) == 0:

                print(allPlayerCards[person][1])
                if (len(allPlayerCards[person][1]) == 0):
                    (playersToRemove).append(person)
                    print(person + " has been eliminated!")
                else:
                    allPlayerCards[person][0].extend(allPlayerCards[person][1])
                    shuffle(allPlayerCards[person][0])
                    allPlayerCards[person][1] = []

        while len(playersToRemove) > 0:
            print(playersToRemove[0])
            print(playersWithCards)
            playersWithCards.remove(playersToRemove[0])
            del playersToRemove[0]

        #this should be done last
        return winningPlayer






    while (len(playersWithCards) > 1):
        round += 1
        roundWinner = playRound((playersWithCards))
        print(roundWinner + " wins Round " + str(round) + "!\n\n\n")
        print(playersWithCards)

    return playersWithCards[0]
