from part_1 import load_input, count_num_options


def parse_input(path):
    content = load_input(path).split("\n")

    time = content[0].split()[1:]
    final_time = int(''.join(time))

    distance = content[1].split()[1:]
    final_distance = int(''.join(distance))
    return final_time, final_distance


time, distance = parse_input("input.txt")
print(count_num_options(time, distance))
