input_file = open("input.txt", "r")
text_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def first_digit(line):
    if line[0].isdigit():
        return int(line[0])

    if not line.startswith(tuple(text_digits)):
        return 0

    for digit in text_digits:
        if line.startswith(digit):
            return text_digits.index(digit) + 1


def last_digit(line):
    if line[-1].isdigit():
        return int(line[-1])

    if not line.endswith(tuple(text_digits)):
        return 0

    for digit in text_digits:
        if line.endswith(digit):
            return text_digits.index(digit) + 1


def get_first_digit(line):
    while len(line):
        digit = first_digit(line)
        if digit != 0:
            return digit
        line = line[1:]
    return 0


def get_last_digit(line):
    while len(line):
        digit = last_digit(line)
        if digit != 0:
            return digit
        line = line[:-1]
    return 0


output = sum(int(str(get_first_digit(line)) + str(get_last_digit(line))) for line in input_file)

print(output)
