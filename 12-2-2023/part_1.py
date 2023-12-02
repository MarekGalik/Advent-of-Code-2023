def is_cubes_enough(color, amount):
    cubes_amount = {'red': 12, 'green': 13, 'blue': 14}
    return cubes_amount[color] >= amount


def check_batch(batch):
    bags = batch.split(',')
    for bag in bags:
        cubes = bag.split()
        if not is_cubes_enough(cubes[1], int(cubes[0])):
            return False
    return True


def check_line(line):
    line_parts = line.split(':')
    game_id = int(line_parts[0].split()[1])
    batches = line_parts[1].split(';')
    return next((0 for batch in batches if not check_batch(batch)), game_id)


def check_file(file):
    return sum(check_line(line) for line in file)


print(check_file(open("test.txt", "r")))
