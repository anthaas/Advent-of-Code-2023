#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

parsed = [x.split(": ")[1].replace(" ", "") for x in lines]
time = eval(parsed[0])
distance = eval(parsed[1])
records = 0

for i in range(time+1):
    run = i * (time-i)
    if run > distance:
        records += 1

print(records)
