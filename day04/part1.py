#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

parsed = [x.split(": ")[1].split(" | ") for x in lines]
intersect_size = [len(list(set(filter(None, x[0].split(" "))) & set(filter(None, x[1].split(" "))))) for x in parsed]
result = sum([2 ** (x - 1) if x > 0 else 0 for x in intersect_size])
print(result)
