def load_lines():
    file = open("test.txt")
    lines = file.readlines()
    file.close()
    return lines


def get_position_of_lowest_digit(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return i
    return len(line)+1
        

def get_position_of_highest_digit(line):
    highest_digit = -1
    for i in range(len(line)):
        if line[i].isdigit():
            if i > highest_digit:
                highest_digit = i
    return highest_digit


#returns the position of the first letter of the first worded number or the first digit, and the first letter of the last, or the last digit
def get_positions_of_numbers(line):
    lowest = get_position_of_lowest_digit(line)
    highest = get_position_of_highest_digit(line)
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
   
    for word_number in numbers:
        if line.rfind(word_number) < lowest and line.find(word_number) != -1:
            lowest = line.rfind(word_number)
        if line.find(word_number) < lowest and line.find(word_number) != -1:
            lowest = line.find(word_number)
        if line.find(word_number) > highest:
            highest = line.find(word_number)
        if line.rfind(word_number) > highest:
            highest = line.rfind(word_number)
    return [lowest, highest]


def getDigitAtI(line, pos):
    if line[pos].isdigit():
        return line[pos]
    
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

    word_number = ""
    flag = False
    for i in range(pos, len(line)):
        if i == pos:
            word_number = line[i]
        else:
            word_number = word_number + line[i]
            if word_number in numbers:
                return numbers.index(word_number)+1
    return ""

#lowest and highest pos are right
def get_digit_including_numbers(line):
    low_high_list = get_positions_of_numbers(line)
    lowest_pos = low_high_list[0]
    if len(low_high_list) > 1:
       highest_pos = low_high_list[1]
    else:
        highest_pos = low_high_list[0]
    return int(str(getDigitAtI(line, lowest_pos)) + str(getDigitAtI(line, highest_pos)))


    
def get_final_value():
    total = 0
    lines = load_lines()
    for line in lines:
        print("line", line)
        print("digit:", get_digit_including_numbers(line))
        total += get_digit_including_numbers(line)
    return total

print(get_final_value())


