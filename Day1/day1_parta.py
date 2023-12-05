def load_lines():
    file = open("input.txt")
    lines = file.readlines()
    file.close()
    return lines
'''
#gets the first digit and the second digit of a line,
#combines them and returns them as int
def get_digit(line):
    list_digits = []
    for char in line:
        if char.isdigit():
            list_digits.append(char)
    return int(list_digits[0] + list_digits[-1])
'''

def get_digit_including_numbers(line):
    list_digits = []
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    word_number = ""
    for char in line:
        if char.isdigit():
            list_digits.append(char)
        else:
            word_number.append(char)
            if word_number in numbers:
                list_digits.append(numbers.index(word_number)+1)
                word_number = "" 

    
def get_final_value():
    total = 0
    lines = load_lines()
    for line in lines:
        total += get_digit(line)
    return total

print(get_final_value())
