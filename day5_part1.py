
#pass in the first line and get a list of seed values
def getSeedList(line):
    lineParts = line.split()
    seedList = lineParts[1:]
    return seedList

#starts with seed-to-soil map and follows trail to get location number
def followTrailForLocationNumber(lines, seedNumber):
    listTitle = []
    currentSet = []
    listSets = []
    for line in lines:
        if "-to-" in line:
            listTitle.append(line)
            if len(currentSet) != 0:
                listSets.append(currentSet)
            currentSet = []
        elif not "seeds" in line:
            currentSet.append(line)
    listSets.append(currentSet)

    newCode = seedNumber
    for i in range(len(listTitle)):
        newCode = convertThroughRange(newCode, listSets[i])
    #never finishing the forloop
    return newCode

#pass in the lines describing a range and the sourceNumber and get the destination number
def convertThroughRange(seedNumber, rangeLines):
    newSeedNumber = int(seedNumber)
    for line in rangeLines:
        lineComponents = line.split()
        destRangeStart = int(lineComponents[0])
        sourceRangeStart = int(lineComponents[1])
        rangeLength = int(lineComponents[2])
        if int(seedNumber) >= sourceRangeStart and int(seedNumber) < sourceRangeStart + rangeLength:
           newSeedNumber = int(seedNumber) + (destRangeStart - sourceRangeStart)
    return newSeedNumber

#takes lines, generates list of location numbers
def getLocationNumberList(lines):
    locationNumber = []
    seedList = getSeedList(lines[0])
    for seedNumber in seedList:
        locationNumber.append(followTrailForLocationNumber(lines, seedNumber))

    return locationNumber

def getLowestLocationNumber(lines):
    locationNumbers = getLocationNumberList(lines)
    lowestLocation = min(locationNumbers)
    return lowestLocation

with open("day5_actual_input.txt", "r") as myFile:
    lines = myFile.readlines()
    linesStripped = []
    for line in lines:
        if line != "\n":
            linesStripped.append(line.strip())

    print(getLowestLocationNumber(linesStripped))




