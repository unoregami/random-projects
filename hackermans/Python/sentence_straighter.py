sentence = ""
while True:
    x = input("x: ")
    if x == "":
        break
    sentence += x

with open('Common_Words.txt', 'w') as f:
    f.write(sentence)