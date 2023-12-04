def load_input(path):
    file = open(path, 'r')
    return list(file)


def extract_lists(card):
    parts = card.split(':')
    lists = parts[1].split('|')
    winning_numbers = extract_numbers(lists[0])
    given_numbers = extract_numbers(lists[1])
    return [winning_numbers, given_numbers]


def extract_numbers(part):
    return [int(i) for i in part.split()]


def count_points(card):
    points = 0
    for number in card[0]:
        if number in card[1]:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points


def get_solution(file):
    output = 0
    for line in file:
        card = extract_lists(line)
        print(count_points(card))
        output += count_points(card)
    return output


input_file = load_input("input.txt")
print(get_solution(input_file))
