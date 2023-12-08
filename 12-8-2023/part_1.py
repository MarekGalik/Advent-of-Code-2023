def load_input(path):
    with open(path, 'r') as file:
        return file.read().splitlines()


def parse_moves(line):
    parts = line.split("=")
    moves = parts[1].split(",")
    node = parts[0].strip()
    return node, {
        "L": moves[0][2:5],
        "R": moves[1][:-1].strip()
    }


def traverse_map(mapping, directions):
    index = 0
    current = "AAA"
    while current != "ZZZ":
        current = mapping[current][directions[index % len(directions)]]
        index += 1
    return index


content = load_input("input.txt")
directions = content[0]

mapping = dict(parse_moves(line) for line in content[2:])

index = traverse_map(mapping, directions)
print(index)
