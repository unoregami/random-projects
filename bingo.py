import random
import time


bola = []
def reloadBola(bola):   # reset bola
    bola.clear()
    for i in range(75):
        bola.append(i+1)
    return bola

def bunotBola(bola):    # bunot bola and removes num from choices
    print("Bunoting...")
    # time.sleep(3)
    choice = random.choice(bola)
    bola.remove(choice)
    if choice <= 15:
        print("B", end="")
    elif choice <= 30:
        print("I", end="")
    elif choice <= 45:
        print("N", end="")
    elif choice <= 60:
        print("G", end="")
    else:
        print("O", end="")

    print(f"{choice}!")
    return choice

def populateCard(): # create bingo card
    card = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": []
    }
    for letter in card:
        for i in range(5):
            num = 0
            match letter:
                case "B":
                    while num == 0 or num in card[letter]:
                        num = random.randint(1,15)
                case "I":
                    while num == 0 or num in card[letter]:
                        num = random.randint(16,30)
                case "N":
                    while num == 0 or num in card[letter]:
                        num = random.randint(31,45)
                case "G":
                    while num == 0 or num in card[letter]:
                        num = random.randint(46,60)
                case "O":
                    while num == 0 or num in card[letter]:
                        num = random.randint(61,75)
            card[letter].append(num)
    return card

def displayCard(card):  # display bingo card in a readable format
    print("B\tI\tN\tG\tO")
    cardNum = ""
    for i in range(5):
        for letter in card:
            cardNum = cardNum + str(card[letter][i]) + "\t"
        cardNum = cardNum + "\n"

    print(cardNum)

def checkCardForNum(card, bunot):  # check bunot to bingo card
    for letter in card:
        for i in range(len(card[letter])):
            if card[letter][i] == bunot:
                card[letter][i] = "★"
                return card
    return card

def isBingo(card): # checks card if bingo
    starNumIndex = []
    for letter in card:
        for i in range(len(card[letter])):
            if card[letter][i] == "★":
                starNumIndex.append(i)
    # Horizontal Bingo
    for i in range(5):
        bingo = starNumIndex.count(i)
        if bingo == 5:
            return True
    
    # Slanted Bingo
    if card["B"][0] == "★" and card["I"][1] == "★" and card["N"][2] == "★" and card["G"][3] == "★" and card["O"][4] == "★":
        return True
    if card["B"][4] == "★" and card["I"][3] == "★" and card["N"][2] == "★" and card["G"][1] == "★" and card["O"][0] == "★":
        return True
    
    return False

def isBlackout(card):   # checks if card is blackout bingo
    pass


bola = reloadBola(bola)

card = populateCard()
displayCard(card)
bunotCount = 0
while True:
    bunot = bunotBola(bola)
    bunotCount += 1
    card = checkCardForNum(card, bunot)
    displayCard(card)
    if isBingo(card):
        print("""▄▄▄▄▄▄▄   ▄▄▄▄▄ ▄▄▄    ▄▄▄  ▄▄▄▄▄▄▄    ▄▄▄▄▄    ▄▄ 
███▀▀███▄  ███  ████▄  ███ ███▀▀▀▀▀  ▄███████▄  ██ 
███▄▄███▀  ███  ███▀██▄███ ███       ███   ███  ██ 
███  ███▄  ███  ███  ▀████ ███  ███▀ ███▄▄▄███  ▀▀ 
████████▀ ▄███▄ ███    ███ ▀██████▀   ▀█████▀   ██ """)
        print("Bunot Count:", bunotCount)
        break