#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

parsed = [x.split(": ")[1].split() for x in lines]
time = [eval(i) for i in parsed[0]]
distance = [eval(i) for i in parsed[1]]
init = 1

for t, d in zip(time, distance):
    records = 0
    for i in range(t+1):
        run = i * (t-i)
        if run > d:
            records += 1
    init *= records

print(init)
