def load_input(path):
    file = open(path, 'r')
    return list(file)


def get_solution(content):
    counter = {}
    for card in content:
        tmp = card.split(":")
        card_number = int(tmp[0].split()[1])

        if card_number not in counter:
            counter[card_number] = 0

        counter[card_number] += 1
        all_numbers = tmp[1]
        numbers = all_numbers.split("|")
        winning_numbers = numbers[0].split()
        your_numbers = numbers[1].split()

        copies = sum(number in winning_numbers for number in your_numbers)
        for i in range(1, copies + 1):
            if (card_number + i) not in counter:
                counter[card_number + i] = 0
            counter[card_number + i] += counter[card_number]

    return sum(counter.values())


input_file = load_input("input.txt")
print(get_solution(input_file))
