def check_batch(batch):
    amounts = {}
    bags = batch.split(',')
    for bag in bags:
        cubes = bag.split()
        amounts[cubes[1]] = int(cubes[0])
    return amounts


def recount_minimum_amounts(minimum_amounts, amounts):
    for color in amounts:
        if amounts[color] > minimum_amounts[color]:
            minimum_amounts[color] = amounts[color]
    return minimum_amounts


def count_power(amounts):
    output = 1
    for a in amounts.values():
        output *= a
    return output


def check_line(line):
    minimum_amounts = {'red': 0, 'green': 0, 'blue': 0}
    line_parts = line.split(':')
    batches = line_parts[1].split(';')
    for batch in batches:
        line_amounts = check_batch(batch)
        minimum_amounts = recount_minimum_amounts(minimum_amounts, line_amounts)
    return count_power(minimum_amounts)


def check_file(file):
    return sum(check_line(line) for line in file)


print(check_file(open("input.txt", "r")))
