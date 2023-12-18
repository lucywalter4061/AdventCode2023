



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

    #checks if a coordinate is next to a symbol
    def isCoordNextToSymbol(self, listRowColumn):
        for row in range(listRowColumn[0]-1, listRowColumn[0] + 2):
            for column in range(listRowColumn[1]-1, listRowColumn[1] + 2):
                if not self.isOutOfRange(row, column):
                    if self.isSymbol(number.lines[row][column]):
                        return True
        return False


    #returns True if number is next to a symbol
    def isPartNumber(self):
        for i in range(self.column_start, self.column_end+1):
            if self.isCoordNextToSymbol([self.row, i]):
                return True
        return False
        


    def isOutOfRange(self, intRow, intColumn):
        return intRow < 0 or intColumn < 0 or intRow >= number.noRows or intColumn >= number.noColumns
            

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


    numbers = number.getsNumbers()

    total = 0
    for n in numbers:
        if n.isPartNumber():
            total += n.number
    return total


print(getSolution())

