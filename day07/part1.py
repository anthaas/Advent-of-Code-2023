#!/usr/bin/env python3
from enum import Enum

with open('input.txt') as f:
    lines = f.read().splitlines()

CARD_STRENGTH = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_KIND = 6
    FIVE_OF_KIND = 7


def get_hand_type(cards):
    card_values = sorted({item: cards.count(item) for item in cards}.items(), key=lambda x: x[1], reverse=True)
    if (card_values[0][1] == 5):
        return HandType.FIVE_OF_KIND.value
    elif (card_values[0][1] == 4):
        return HandType.FOUR_OF_KIND.value
    elif (card_values[0][1] == 3 and card_values[1][1] == 2):
        return HandType.FULL_HOUSE.value
    elif (card_values[0][1] == 3):
        return HandType.THREE_OF_KIND.value
    elif (card_values[0][1] == 2 and card_values[1][1] == 2):
        return HandType.TWO_PAIR.value
    elif (card_values[0][1] == 2):
        return HandType.ONE_PAIR.value
    else:
        return HandType.HIGH_CARD.value


# order by multiple criteria 1. hand type, 2. card strength
sorted_games = sorted(lines,
                      key=lambda x: (get_hand_type(x.split()[0]), [CARD_STRENGTH.index(ch) for ch in x.split()[0]]))
result = sum([(i + 1) * int(x.split()[1]) for i, x in enumerate(sorted_games)])
print(result)
