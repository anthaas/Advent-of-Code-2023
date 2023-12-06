#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

parsed = [x.split(": ")[1].replace(" ", "") for x in lines]
time = int(parsed[0])
distance = int(parsed[1])
result = sum(1 for i in range(time + 1) if i * (time - i) > distance)
print(result)
