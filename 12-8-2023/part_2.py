from math import gcd
from part_1 import load_input


def parse_moves(line):
    parts = line.split("=")
    moves = parts[1].split(",")
    node = parts[0].strip()
    return node, {
        "L": moves[0][2:5],
        "R": moves[1][:-1].strip()
    }


def find_currents(mapping):
    return [node for node in mapping if node.endswith("A")]


def find_loops(mapping, currents, directions):
    loops = []
    for current in currents:
        loop = []

        counter = 0
        first_goal = None
        while True:
            while counter == 0 or not current.endswith("Z"):
                current = mapping[current][directions[counter % len(directions)]]
                counter += 1
            loop.append(counter)
            if not first_goal:
                first_goal = current
                counter = 0
            elif current == first_goal:
                break
        loops.append(loop)

    return [loop[0] for loop in loops]


def calculate_lcm(loops):
    lcm = 1
    for i in loops:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


content = load_input("input.txt")
directions = content[0]

mapping = dict(parse_moves(line) for line in content[2:])

currents = find_currents(mapping)

loops = find_loops(mapping, currents, directions)
lcm = calculate_lcm(loops)

print(lcm)
