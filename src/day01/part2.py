#!/usr/bin/env python3

WORDS_TO_NUMBERS = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine"
}


def replace_all_from_dictionary(text):
    for key, value in WORDS_TO_NUMBERS.items():
        text = text.replace(key, value)
    return text


with open('input.txt') as f:
    lines = f.read().splitlines()
substituted = [replace_all_from_dictionary(line) for line in lines]
# filter only digits for each line
filtered = [[c for c in line if c.isdigit()] for line in substituted]
selected = [int(x[0] + x[-1]) for x in filtered]
print(sum(selected))
