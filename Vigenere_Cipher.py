from string import ascii_uppercase
import random
import re


def encode_text(text:str, key:str):
    while len(key) < len(text): # Repeat concat key until longer than text
        key += key
    encripted = ""
    for i in range(len(text)):
        indexY = x.index(text[i])   # Finds Y index using text char
        indexX = y.index(key[i])    # Finds X index using key char
        encripted += table[indexX][indexY]  # Stores the intercepting cipher char
    return encripted

def decrypt_text(cipher:str, key:str):
    while len(key) < len(cipher):
        key += key
    decrypted = ""
    for i in range(len(cipher)):
        indexX = y.index(key[i])    # Finds X index using key char
        indexY = table[indexX].index(cipher[i]) # Finds Y index using table and cipher char
        decrypted += x[indexY]  # Therefore finding the plaintext char
    return decrypted

def pick_cypher_table(user:str):
    match user:
        case "1":   # Normal
            x = list(ascii_uppercase)
            xOrig = x.copy()
            y = x.copy()
        case "2":   # Random y
            x = list(ascii_uppercase)
            xOrig = x.copy()
            y = list()
            for i in range(len(x)):
                ph = x[random.randrange(0, len(x))]
                while ph in y:
                    ph = x[random.randrange(0, len(x))]
                y.append(ph)
        case "3":   # Random plaintext
            x = list()
            y = list(ascii_uppercase)
            for i in range(len(y)):
                ph = y[random.randrange(0, len(y))]
                while ph in x:
                    ph = y[random.randrange(0, len(y))]
                x.append(ph)
            xOrig = x.copy()
        case "4":   # Both random
            x = list()
            y = list()
            for i in range(len(ascii_uppercase)):
                ph = ascii_uppercase[random.randrange(0, len(ascii_uppercase))]
                while ph in x:
                    ph = ascii_uppercase[random.randrange(0, len(ascii_uppercase))]
                x.append(ph)
    
                ph = ascii_uppercase[random.randrange(0, len(ascii_uppercase))]
                while ph in y:
                    ph = ascii_uppercase[random.randrange(0, len(ascii_uppercase))]
                y.append(ph)
            xOrig = x.copy()
        case _:
            print("ERROR")
    return x, xOrig, y


# Initialize x and y
table = list()
print("[1 - normal | 2 - rand Y | 3 - rand X | 4 - rand XY]")
user = input("Type: ")
x,xOrig,y = pick_cypher_table(user) # xOrig to retain default plaintext after augmentation



# Build and visualize the table
print("    ", end="")
for i in x:
    print(i, end=" ")
print("\n")

for i in range(len(x)):
    if i == 0:
        ph = x.copy()
        print(f"{y[i]}   ", end="")
        for j in range(len(ph)):
            print(ph[j], end=" ")
        print()
        table.append(ph)
        continue
    ph = x[1:].copy()
    ph.append(x[0])
    x = ph
    print(f"{y[i]}   ", end="")
    for j in range(len(ph)):
        print(ph[j], end=" ")
    print()
    table.append(ph)
x = xOrig.copy()
print()

# Test
text = re.sub(" +", "", input("").upper())  # allows whitespace input
key = input("Key: ").upper()
cipher = encode_text(text, key)

print()
print(cipher)
print(decrypt_text(cipher, key))



