#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

parsed = [x.split(": ")[1].split(" | ") for x in lines]
intersect_size = [len(list(set(filter(None, x[0].split(" "))) & set(filter(None, x[1].split(" "))))) for x in parsed]
instances = [1 for x in intersect_size]
for i, times in enumerate(intersect_size):
    for j in range(i+1, i+1+times):
        instances[j] += instances[i]

print(sum(instances))

