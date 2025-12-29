import random as rd

def findHighestNum(array):
    highest = array[0]
    for i in array:
        if highest < i:
            highest = i
    return highest

def numToString(array, highestNumLength):
    # convert all len(number) == highestNumLength
    output = list()
    for i in array:
        strNum = str(i)
        while len(strNum) != highestNumLength:
            strNum = f"0{strNum}"
        output.append(strNum)
    return output

def radixSort(array):
    highestNumLength = len(str(findHighestNum(array)))
    index = highestNumLength - 1
    strNumList = numToString(array, highestNumLength)
    print(strNumList)
    print()


    while index >= 0:
        phList = [[],[],[],[],[],[],[],[],[],[]]    # holds the number based on index

        for j in strNumList:
            indexNum = int(j[index])
            phList[indexNum].append(j)

        print(phList)
        print()

        strNumList.clear()
        for j in phList:
            for k in j:
                strNumList.append(k)

        print(strNumList)
        print()

        index -= 1

    # convert strNum back to integer
    array.clear()
    for i in strNumList:
        array.append(int(i))

    return array


sample = list()
for i in range(25):
    sample.append(rd.randrange(0, 300))

print(sample)
print()

print(radixSort(sample))