import random
import time
from string import ascii_uppercase

def displayCard(num, suit): # show card
    card = f""" _____
|{num}{suit}   |
|     |
|     |
|_____|"""
    
    return card

def dealBacarrat(deck): # deal bacarrat
    bacarrat = []
    player = 0
    banker = 0
    soloAnimCopy = soloAnim.copy()
    for i in range(4):
        time.sleep(2)
        # get card from deck
        randNum = random.randrange(0, len(deck))
        bacarrat.append(deck[randNum])
        deck.pop(randNum)

        # real num values
        num = bacarrat[i][0]
        if num in ascii_uppercase:       # turn letter into corres. nums
            if num > "A":
                num = 10
            else:
                num = 1
        num = int(num)

        if i % 2 == 0:  # player
            player += num
        else:           # banker
            banker += num

        # populate card animation
        for j in range(len(soloAnimCopy)):
            soloAnimCopy[j] = soloAnimCopy[j].replace(f"{i+1}{chr(ord('`')+i+1)}", f"{bacarrat[i][0]}{bacarrat[i][1]}")
        
        print(f"PLAYER ({player})\t\tBANKER ({banker})")
        print(soloAnimCopy[i])
        
    
    winner = 0
    if str(player)[-1] > str(banker)[-1]:
        winner = 0
    elif str(player)[-1] < str(banker)[-1]:
        winner = 1
    else:
        winner = 2

    return deck, winner


# =========== ANIMATIONS =============
# 1a = first card's num and suit | 2b = 2nd | 3c = 3rd | 4d = 4th

blank_card1 = """ _____ 
|     |
|     |
|     |
|_____|
"""

blank_card2 = """ _____ \t\t\t _____ 
|     |\t\t\t|     |
|     |\t\t\t|     |
|     |\t\t\t|     |
|_____|\t\t\t|_____|
"""

blank_card3 = """ _____   _____ \t\t _____
|     | |     |\t\t|     |
|     | |     |\t\t|     |
|     | |     |\t\t|     |
|_____| |_____|\t\t|_____|
"""

blank_card4 = """ _____   _____ \t\t _____   _____ 
|     | |     |\t\t|     | |     |
|     | |     |\t\t|     | |     |
|     | |     |\t\t|     | |     |
|_____| |_____|\t\t|_____| |_____|
"""

populated_card1 = """ _____   _____ \t\t _____   _____ 
|1a   | |     |\t\t|     | |     |
|     | |     |\t\t|     | |     |
|     | |     |\t\t|     | |     |
|_____| |_____|\t\t|_____| |_____|
"""

populated_card2 = """ _____   _____ \t\t _____   _____ 
|1a   | |     |\t\t|2b   | |     |
|     | |     |\t\t|     | |     |
|     | |     |\t\t|     | |     |
|_____| |_____|\t\t|_____| |_____|
"""

populated_card3 = """ _____   _____ \t\t _____   _____ 
|1a   | |3c   |\t\t|2b   | |     |
|     | |     |\t\t|     | |     |
|     | |     |\t\t|     | |     |
|_____| |_____|\t\t|_____| |_____|
"""

populated_card4 = """ _____   _____ \t\t _____   _____ 
|1a   | |3c   |\t\t|2b   | |4d   |
|     | |     |\t\t|     | |     |
|     | |     |\t\t|     | |     |
|_____| |_____|\t\t|_____| |_____|
"""

solo_card1 = """ _____ 
|1a   |
|     |
|     |
|_____|
"""

solo_card2 = """ _____ \t\t\t _____ 
|1a   |\t\t\t|2b   |
|     |\t\t\t|     |
|     |\t\t\t|     |
|_____|\t\t\t|_____|
"""

solo_card3 = """ _____   _____ \t\t _____
|1a   | |3c   |\t\t|2b   |
|     | |     |\t\t|     |
|     | |     |\t\t|     |
|_____| |_____|\t\t|_____|
"""

solo_card4 = """ _____   _____ \t\t _____   _____ 
|1a   | |3c   |\t\t|2b   | |4d   |
|     | |     |\t\t|     | |     |
|     | |     |\t\t|     | |     |
|_____| |_____|\t\t|_____| |_____|
"""

blankAnim = [blank_card1, blank_card2, blank_card3, blank_card4]
populatedAnim = [populated_card1, populated_card2, populated_card3, populated_card4]
soloAnim = [solo_card1, solo_card2, solo_card3, solo_card4]
# ====================================


# builds the deck
suit = ["♦️","♠️","❤️","♣️"]
deck = []
for i in suit:
    for j in range(13):
        card = f"{j+1}{i}"
        match j:
            case 0:
                card = f"A{i}"
            case 9:
                card = f"X{i}"
            case 10:
                card = f"J{i}"
            case 11:
                card = f"Q{i}"
            case 12:
                card = f"K{i}"
        deck.append(card)
print("Shuffling...")
time.sleep(5)

# play bacarrat (test run)
cash = 2500
highscore = cash
while len(deck) / 4 > 0:
    if cash <= 0:
        break
    print(f"Cash: {cash}")

    side = input("0 = PLAYER | 1 = BANKER | 2 = TIE\n")
    while side not in ["0", "1", "2"]:
        print("Invalid choice.")
        side = input("0 = PLAYER | 1 = BANKER | 2 = TIE\n")
    
    bet = int(input("Bet: "))
    while bet == 0 or bet > cash:
        print(f"Not enough cash ({cash} remaining)")
        bet = int(input("Bet:"))
    cash -= bet

    deck, winner = dealBacarrat(deck)

    match winner:
        case 0:
            print("PLAYER WON")
            if side == "0":
                cash += bet * 2
                print("WON", bet * 2)
        case 1:
            print("BANKER WON")
            if side == "1":
                cash += bet * 2
                print("WON", bet * 2)
        case 2:
            print("TIE")
            if side == "2":
                cash += bet * 8
                print("WON", bet * 8)
            else:
                cash += bet
                print("WON", bet)
    
    if cash > highscore:
        highscore = cash

print("DECK IS GONE")
print(f"Highscore: {highscore}")
