
#load lines in from file
def loadLines():
    with open("day5_mytest_input.txt", "r") as myFile:
        lines = myFile.readlines()
        linesStripped = [line.strip() for line in lines if line != "\n"]
    return linesStripped

#returns list of the seed numbers
def getSeeds(line):
    lineParts = line.split()
    seedList = lineParts[1:]
    return seedList

#takes the seed and range details, returns the amended seed range as a list of new ranges (seed start, range value)
def processSeedsWithRange(lowerSeedValue, seedRange, lowerChangeValue, changeRange, newValue):
    upperSeedValue = lowerSeedValue + seedRange - 1
    upperChangeValue = lowerChangeValue + changeRange - 1
    adjustment = newValue - lowerSeedValue #add this on to new range values

    if lowerSeedValue >= lowerChangeValue:
        if upperSeedValue <= upperChangeValue:
            print("here")
            #range from lower seed value to upper seed value
            return [lowerSeedValue + adjustment, seedRange]
        else:
            print("a")
            return [lowerSeedValue + adjustment, upperChangeValue - lowerSeedValue + 1] + [upperChangeValue+1, upperSeedValue - upperChangeValue]
    else:
        if upperSeedValue >= lowerChangeValue:
            if upperSeedValue <= upperChangeValue:
                return [lowerSeedValue, lowerChangeValue - lowerSeedValue] + [lowerChangeValue + adjustment,  upperSeedValue - lowerChangeValue + 1]
            else:
                return [lowerSeedValue, lowerChangeValue - lowerSeedValue ] + [lowerChangeValue + adjustment, upperChangeValue - lowerChangeValue + 1] + [upperChangeValue + 1, upperSeedValue - upperChangeValue]
    return [lowerSeedValue, seedRange]

#takes the starting range, applies the new maps and returns seed ranges
#mapCodes take the form [50, 98, 2], figure to adjust to, start of range, length of range
def apply_maps(startSeedList, mapList):
    newSeedList  = []
    for i in range(len(startSeedList)):
        if i%2 == 0:
            for mapCode in mapList:
                mapCodeSplit = mapCode.split()
                rangesToAdd = processSeedsWithRange(int(startSeedList[i]), int(startSeedList[i+1]), int(mapCodeSplit[1]), int(mapCodeSplit[2]), int(mapCodeSplit[0]))
                print(rangesToAdd)
                newSeedList = newSeedList + rangesToAdd
    return newSeedList

#makes a list of lists of maps as a 2d array
def getMapLists(lines):
    currentSet = []
    listSets = []

                 
    for line in lines:
        if not "-to-" in line and not "seeds" in line:
            currentSet.append(line)
    listSets.append(currentSet)
    return listSets

#gets the lowest location from a range in form 79 14 55 13
def getLowestLocationFromRange(locationList):
    listToCheck = []
    print(locationList)
    for i in range(len(locationList)):
        if i % 2 == 0:
            listToCheck.append(locationList[i])

    minLocation = min(listToCheck)
    return minLocation


def solve():
    lines = loadLines()
    newSeedRange = getSeeds(lines[0])
    mapLists = getMapLists(lines)
    for mapList in mapLists:
       newSeedRange = apply_maps(newSeedRange, mapList)
    print("New seed range: ", newSeedRange)
    print(getLowestLocationFromRange(newSeedRange))

solve()
       #print(def processSeedsWithRange(lowerSeedValue, seedRange, lowerChangeValue, changeRange, newValue):)
#print(processSeedsWithRange(5, 2, 20, 4, 6)) #no overlap test /
#print(processSeedsWithRange(3, 3, 4, 3, 4)) #lower seed lower than lower change but higher seed higher than lower change and lower than upper change test /
#print(processSeedsWithRange(4, 7, 7, 2, 5)) #lower seed lower than lower change and higher seed higher than lower change and higher than upper change test x /
#print(processSeedsWithRange(4, 5, 3, 7, 5)) #lower seed higher than lower change and higher seed lower than higher change test  /
#print(processSeedsWithRange(2, 5, 1, 4, 3)) #lower seed higher than lower change and higher seed higher than higher chagne test x /


