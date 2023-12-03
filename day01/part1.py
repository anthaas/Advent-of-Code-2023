#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

# filter only digits for each line
filtered = [[c for c in line if c.isdigit()] for line in lines]
selected = [int(x[0] + x[-1]) for x in filtered]
print(sum(selected))
