def load_input(path):
    with open(path, 'r') as file:
        return file.read()


def parse_input(path):
    content = load_input(path).split("\n")

    time = content[0].split()[1:]
    time = [int(x) for x in time]

    distance = content[1].split()[1:]
    distance = [int(x) for x in distance]
    return time, distance


def count_num_options(time, distance):
    return sum(sec * (time - sec) > distance for sec in range(1, time))


def get_solution(time, distance):
    result = 1
    for time, distance in zip(time, distance):
        result *= count_num_options(time, distance)
    return result


time, distance = parse_input("input.txt")
print(get_solution(time, distance))
