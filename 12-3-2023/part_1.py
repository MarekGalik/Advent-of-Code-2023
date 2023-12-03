def load_input(path):
    input_file = open(path, 'r')
    return list(input_file)


def find_first_number(line, start_position):
    first = -1
    last = -1
    for i in range(start_position, len(line)):
        if line[i].isdigit():
            if first == -1:
                first = last = i
            else:
                last = i

        elif not line[i].isdigit() and last != -1:
            break
    return first, last


def is_allowed_symbol(char):
    return not char.isdigit() and char != '.'


def check_left(line, start):
    return False if start < 1 else bool(is_allowed_symbol(line[start - 1]))


def check_right(line, end):
    return False if end > len(line) - 2 else bool(is_allowed_symbol(line[end+1]))


def check_top(input, line_index, start, end):
    if line_index == 0:
        return False
    start = max(start, 1)
    if end > len(input[line_index]) - 2:
        end = len(input[line_index]) - 2
    return any(is_allowed_symbol(input[line_index - 1][i]) for i in range(start - 1, end + 1))


def check_bottom(input, line_index, start, end):
    if line_index >= len(input) - 1:
        return False
    start = max(start, 1)
    if end > len(input[line_index]) - 2:
        end = len(input[line_index]) - 2
    return any(is_allowed_symbol(input[line_index + 1][i]) for i in range(start - 1, end + 1))


def get_solution(input_path):
    input = load_input(input_path)
    output = 0
    for index, line in enumerate(input):
        start_position = 0
        while start_position < len(line):
            start, end = find_first_number(line, start_position)
            if start == -1:
                break
            number = line[start:end + 1]
            if check_left(line, start) \
                    or check_right(line, end) \
                    or check_top(input, index, start, end+1) \
                    or check_bottom(input, index, start, end+1):
                output += int(number)
            start_position = end + 1


print(get_solution("input.txt"))
