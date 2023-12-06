#!/usr/bin/env python3
from functools import reduce

with open('input.txt') as f:
    lines = f.read().splitlines()

parsed = [x.split(": ")[1].split() for x in lines]
time = [eval(i) for i in parsed[0]]
distance = [eval(i) for i in parsed[1]]
records = [sum(1 for i in range(t + 1) if i * (t - i) > d) for t, d in zip(time, distance)]
result = reduce((lambda x, y: x * y), records)
print(result)
