#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

maximum = {"red": 12, "green": 13, "blue": 14}

games = [x.split(": ")[1].split("; ") for x in lines]
result = 0
for index, game in enumerate(games):
    linearized_game = [item.split() for sublist in [x.split(", ") for x in game] for item in sublist]
    if all([int(x[0]) <= maximum.get(x[1]) for x in linearized_game]):
        result += index + 1

print(result)
