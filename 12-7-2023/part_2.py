from part_1 import get_solution


class Hand:
    def __init__(self, card_info):
        card_str, value = card_info.split()
        self.cards = card_str
        self.value = int(value)


def card_strength(card):
    card_order = "J23456789TQKA"
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
        A_priority = 7 if 'J' in cards else 6
    elif len(card_set) == 2:  # 3 same letters with 2 same letters at one
        A_priority = 7 if 'J' in cards else 5
    elif len(card_set) == 3 and (
            cards.count(list(card_set)[0]) == 3 or cards.count(list(card_set)[1]) == 3 or cards.count(
            list(card_set)[2]) == 3):  # 3 same letters
        A_priority = 6 if 'J' in cards else 4
    elif len(card_set) == 3:
        if 'J' in cards and cards.count('J') == 1:
            A_priority = 5
        elif 'J' in cards and cards.count('J') == 2:
            A_priority = 6
        else:
            A_priority = 3
    elif len(card_set) == 4:  # 2 same letters
        A_priority = 4 if 'J' in cards else 2
    else:
        A_priority = 2 if 'J' in cards else 1
    B_priority = hand_strength(cards)

    return A_priority, B_priority


print(get_solution("input.txt", custom_sort))
