def load_lines():
    file = open("day2_part2_input.txt")
    lines = file.readlines()
    file.close()
    return lines


def getGameId(line):
    i = 5
    strId = ""
    while line[i].isdigit():
        strId = strId + line[i]
        i+=1
    return int(strId)

def isLinePossible(line, allowedRed, allowedGreen, allowedBlue):
    possible = True
    sets = line.split(";")
    #Game 20: 4 green, 8 red, 9 blue
    for set in sets:
        rgb = getRGB(set)
        if rgb[0] > allowedRed:
            return False
        if rgb[1]> allowedGreen:
            return False
        if rgb[2] > allowedBlue:
            return False
    return True

#Returns amount of red, green and blue cubes as a list
def getRGB(set):
    intRedAmount = 0
    intGreenAmount = 0
    intBlueAmount = 0

    redPos = set.find("red")
    strRedAmount = ""
    r = redPos - 2
    while set[r].isdigit():
        strRedAmount = set[r] + strRedAmount
        intRedAmount = int(strRedAmount)
        r -= 1
    
    greenPos = set.find("green")
    strGreenAmount = ""
    g = greenPos - 2
    while set[g].isdigit():
        strGreenAmount = set[g] + strGreenAmount
        intGreenAmount = int(strGreenAmount)
        g -= 1

    bluePos = set.find("blue")
    strBlueAmount = ""
    b = bluePos - 2
    while set[b].isdigit():
        strBlueAmount = set[b] + strBlueAmount
        intBlueAmount = int(strBlueAmount)
        b -= 1
    return [intRedAmount, intGreenAmount, intBlueAmount]

def getSolution():
    lines = load_lines()
    total = 0
    for line in lines:
        if isLinePossible(line, 12, 13, 14):
            total += getGameId(line)
    return total


print(getSolution())
            
    
