#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

games = [x.split(": ")[1].split("; ") for x in lines]
result = 0
for game in games:
    rgb = {"red": 0, "green": 0, "blue": 0}
    linearized_game = [item.split() for sublist in [x.split(", ") for x in game] for item in sublist]
    for entry in linearized_game:
        rgb_current_value = rgb[entry[1]]
        current_value = int(entry[0])
        if rgb_current_value < current_value:
            rgb[entry[1]] = current_value
    result += rgb["red"] * rgb["green"] * rgb["blue"]

print(result)
