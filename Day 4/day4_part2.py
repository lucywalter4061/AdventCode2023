def load_lines():
    file = open("day4_actual_input.txt")
    lines = file.readlines()
    file.close()
    return lines

#returns a list of scores (one per line)
def getListScoresForEachLine(lines):
    listScoresForEachLine = []
    
    for line in lines:
        score = 0
        splitLine = line.split(" | ")
        clearWinningNumbers = splitLine[0].strip()
        clearYourNumbers = splitLine[1].strip()
        intListWinningNumbers = clearWinningNumbers.split(" ")
        intListYourNumbers = clearYourNumbers.split(" ")
        
        intListWinningNumbers = intListWinningNumbers[2:]


        for number in intListYourNumbers:
            if number.isdigit() and number in intListWinningNumbers:
                score += 1
        listScoresForEachLine.append(score)
    return listScoresForEachLine

#returns a starting quantity array (all set to 1)
def getQuantityArray(lenLines):
    return [1] * lenLines

def solve(lines):
    listScoresForEachLine = getListScoresForEachLine(lines)
    listQuantitiesForEachLine = getQuantityArray(len(lines))
    for i in range(len(listScoresForEachLine)):
        lineScore = listScoresForEachLine[i]
        for j in range(i + 1, i + 1 + lineScore):
            listQuantitiesForEachLine[j] += listQuantitiesForEachLine[i]
    return getTotalScore(listQuantitiesForEachLine)

#adds up the total number of lines at the end
def getTotalScore(listQuantitiesForEachLine):
    total = 0
    for i in listQuantitiesForEachLine:
        total += i
    return total
        
lines = load_lines()
print(solve(lines))
        
