#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()


def get_next_in_sequence(sequence):
    differences = [sequence]
    actual_line = sequence

    while True:
        next_line = []
        for i in range(len(actual_line) - 1):
            next_line.append(actual_line[i + 1] - actual_line[i])
        differences.append(next_line)
        actual_line = next_line
        if all([x == 0 for x in actual_line]):
            break

    next_in_sequence = 0
    for i in range(len(differences) - 2, -1, -1):
        next_in_sequence = differences[i][0] - next_in_sequence
    return next_in_sequence


result = sum([get_next_in_sequence([int(x) for x in line.split()]) for line in lines])
print(result)
