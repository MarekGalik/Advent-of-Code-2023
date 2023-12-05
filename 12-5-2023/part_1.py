def load_input(path):
    with open(path, 'r') as file:
        return file.read()


def parse_input(input):
    parts = input.split('\n\n')
    parts = [part.strip() for part in parts if part.strip()]

    seeds = parts[0].split()[1:]
    seeds = [int(seed) for seed in seeds]

    mappings = [mapping.split("\n")[1:] for mapping in parts[1:]]
    mappings = [[[int(item) for item in line.split()] for line in mapping] for mapping in mappings]
    return seeds, mappings


def find_destination_number(seed, map):
    for line in map:
        if seed in range(line[1], line[1] + line[2]):
            return line[0] + (seed - line[1])
    return seed


def find_location_number(seed, mappings):
    number = seed
    for map in mappings:
        number = find_destination_number(number, map)
    return number


seeds, mappings = parse_input(load_input("input.txt"))
# print(min(find_location_number(seed, mappings) for seed in seeds))
