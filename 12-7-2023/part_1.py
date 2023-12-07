class Hand:
    def __init__(self, card_info):
        card_str, value = card_info.split()
        self.cards = card_str
        self.value = int(value)


def card_strength(card):
    card_order = "23456789TJQKA"
    return card_order.index(card) + 10


def hand_strength(cards):
    return int(''.join(str(card_strength(card)) for card in cards))


def custom_sort(hand):
    cards = hand.cards
    card_set = set(cards)

    if len(card_set) == 1:  # All five chars are the same
        A_priority = 7
    elif len(card_set) == 2 and (
            cards.count(list(card_set)[0]) == 4 or cards.count(list(card_set)[1]) == 4):  # 4 same letters
        A_priority = 6
    elif len(card_set) == 2:  # 3 same letters with 2 same letters at one
        A_priority = 5
    elif len(card_set) == 3 and (
            cards.count(list(card_set)[0]) == 3 or cards.count(list(card_set)[1]) == 3 or cards.count(
            list(card_set)[2]) == 3):  # 3 same letters
        A_priority = 4
    elif len(card_set) == 3:
        A_priority = 3
    elif len(card_set) == 4:  # 2 same letters
        A_priority = 2
    else:
        A_priority = 1

    B_priority = hand_strength(cards)

    return A_priority, B_priority


def load_input(path):
    with open(path, 'r') as file:
        return file.readlines()


def get_solution(input_path, sort_key):
    hands = [Hand(line.strip()) for line in load_input(input_path)]
    sorted_hands = sorted(hands, key=sort_key)

    return sum(hand.value * (index + 1) for index, hand in enumerate(sorted_hands))


print(get_solution("input.txt", custom_sort))
