def load_lines():
    file = open("day4_actual_input.txt")
    lines = file.readlines()
    file.close()
    return lines

def solve(lines):
    total = 0
    
    for line in lines:
        score = 0
        splitLine = line.split("|")
        clearWinningNumbers = splitLine[0].strip()
        clearYourNumbers = splitLine[1].strip()
        intListWinningNumbers = clearWinningNumbers.split(" ")
        intListYourNumbers = clearYourNumbers.split(" ")
        
        intListWinningNumbers = intListWinningNumbers[2:]


        for number in intListYourNumbers:
            if number.isdigit() and number in intListWinningNumbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total += score
    return total
        

     

lines = load_lines()
print(solve(lines))
        
