input_file = open("input.txt", "r")
output = 0


for line in input_file:
    digits = [int(char) for char in line if char.isdigit()]
    line_sum = str(digits[0]) + str(digits[-1])
    output += int(line_sum)

print(output)
