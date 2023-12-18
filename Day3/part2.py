



class number():
    noRows = 0
    noColumns = 0
    lines = []
    
    def __init__(self, number, row, column_start, column_end):
        self.number = number
        self.row = row
        self.column_start = column_start
        self.column_end = column_end

    def __str__(self):
        return "number: " + str(self.number) + " row: " + str(self.row) + " column_start: " + str(self.column_start) + " column_end: " +  str(self.column_end)
        

    #returns True if item is not digit or .
    def isSymbol(self, char):
        return not char.isdigit() and not char == "."

#returns a list of number objects
def getsNumbers():
    listNumbers = []
    onNumber = False
    strNumber = ""
    start = -1
    for lineNumber in range(len(number.lines)):
        if onNumber:
            listNumbers.append(number(int(strNumber), lineNumber-1, start, char))
        onNumber = False
        for char in range(len(number.lines[lineNumber])):
            if not onNumber:
                if number.lines[lineNumber][char].isdigit():
                    strNumber = number.lines[lineNumber][char]
                    onNumber = True
                    start = char
            else:
                if number.lines[lineNumber][char].isdigit():
                    strNumber = strNumber + number.lines[lineNumber][char]
                else:
                    onNumber = False
                    numberToAdd = number(int(strNumber), lineNumber, start, char-1)
                    listNumbers.append(numberToAdd)
    if onNumber:
        listNumbers.append(number(int(strNumber), lineNumber, start, char))
    return listNumbers

#given a row and column, returns gear ratio if that item is gear, else returns 0
def getGearRatio(row, column, lines, numbers):
    listAdjacentNumbers = []
    if lines[row][column] == "*":
        for number in numbers:
            isAdjacent = False
            if number.row in range (row-1, row+2):
                for i in range(number.column_start, number.column_end + 1):
                    if i in range (column - 1, column + 2):
                        isAdjacent = True
                        break
            if isAdjacent:
                listAdjacentNumbers.append(number)
    if len(listAdjacentNumbers) == 2:
        return listAdjacentNumbers[0].number * listAdjacentNumbers[1].number
    else:
        return 0



def loadLines():
    file = open("day3_final_input.txt")
    lines = file.readlines()
    file.close()
    return lines

def getSolution():
    lines = loadLines()
    linesNoWhiteSpace = []
    
    for line in lines:
        linesNoWhiteSpace.append(line.strip())
        
    number.lines = linesNoWhiteSpace
    number.noRows = len(linesNoWhiteSpace) 
    number.noColumns = len(linesNoWhiteSpace[0])
    total = 0
    numbers = getsNumbers()
    for row in range(number.noRows):
        for column in range(number.noColumns):
            total += getGearRatio(row, column, lines, numbers)
    return total



print(getSolution())

