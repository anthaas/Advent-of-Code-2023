#!/usr/bin/env python3

import math

with open('input.txt') as f:
    parts = f.read().split("\n\n")

instructions = parts[0]
nodes = {}
for x in parts[1].split("\n"):
    parts = x.split(" = ")
    key = parts[0]
    value = parts[1].replace(" ", "")[1:-1].split(",")
    nodes[key] = value

start_nodes = [x for x in nodes.keys() if x[-1] == "A"]
counts = []

for x in start_nodes:
    current_node = x
    steps = 0
    while current_node[-1] != "Z":
        instruction = instructions[steps % len(instructions)]
        steps += 1
        current_node = nodes.get(current_node)[1] if "R" == instruction else nodes.get(current_node)[0]
    counts.append(steps)

print(math.lcm(*counts))
