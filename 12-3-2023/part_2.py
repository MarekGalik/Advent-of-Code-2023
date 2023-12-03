def load_input(path):
    input_file = open(path, 'r')
    return list(input_file)


def find_stars(line):
    return [index for index, char in enumerate(line) if char == '*']


def find_whole_number(top_line, i):
    start = end = i
    new_i = i - 1
    while top_line[new_i].isdigit() and new_i >= 0:
        start = new_i
        new_i -= 1

    new_i = i + 1
    while top_line[new_i].isdigit() and new_i < len(top_line):
        end = new_i
        new_i += 1

    return [start, end]


def find_top_adjacents(input, line_index, line, star_index):
    if line_index == 0:
        return []
    adjacents = []
    top_line = input[line_index - 1]
    for i in range(star_index - 1, star_index + 2):
        if 0 <= i < len(line) and top_line[i].isdigit():
            number = find_whole_number(top_line, i)
            adjacents.append((line_index - 1, number[0], number[1]))
    return adjacents


def find_bottom_adjacents(input, line_index, line, star_index):
    if line_index >= len(input) - 1:
        return []
    adjacents = []
    bottom_line = input[line_index + 1]
    for i in range(star_index - 1, star_index + 2):
        if 0 <= i < len(line) and bottom_line[i].isdigit():
            number = find_whole_number(bottom_line, i)
            adjacents.append((line_index + 1, number[0], number[1]))
    return adjacents


def find_left_adjacent(line, line_index, star_index):
    if line[star_index - 1].isdigit():
        start = end = i = star_index - 1
        while line[i - 1].isdigit() and i >= 1:
            start = i - 1
            i -= 1
        return [(line_index, start, end)]
    return []


def find_right_adjacent(line, line_index, star_index):
    if line[star_index + 1].isdigit():
        start = end = i = star_index + 1
        while line[i + 1].isdigit() and i + 1 < len(line):
            end = i + 1
            i += 1
        return [(line_index, start, end)]
    return []


def get_solution(input_path):
    input = load_input(input_path)
    output = 0
    for line_index, line in enumerate(input):
        star_indexes = find_stars(line)
        for star_index in star_indexes:
            adjacents = find_top_adjacents(input, line_index, line, star_index)
            adjacents += find_bottom_adjacents(input, line_index, line, star_index)
            adjacents += find_left_adjacent(line, line_index, star_index)
            adjacents += find_right_adjacent(line, line_index, star_index)
            adjacents = list(set(adjacents))

            if len(adjacents) == 2:
                output += int(input[int(adjacents[0][0])][int(adjacents[0][1]): int(adjacents[0][2]) + 1]) \
                          * int(input[int(adjacents[1][0])][int(adjacents[1][1]): int(adjacents[1][2]) + 1])


print(get_solution("input.txt"))
