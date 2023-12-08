#!/usr/bin/env python3
from enum import Enum

with open('input.txt') as f:
    parts = f.read().split("\n\n")

instructions = parts[0]
nodes = {}
for x in parts[1].split("\n"):
    parts = x.split(" = ")
    key = parts[0]
    value = parts[1].replace(" ", "")[1:-1].split(",")
    nodes[key] = value

current_node = "AAA"
steps = 0
while current_node != "ZZZ":
    instruction = instructions[steps % len(instructions)]
    steps += 1
    current_node = nodes.get(current_node)[1] if "R" == instruction else nodes.get(current_node)[0]

print(steps)
