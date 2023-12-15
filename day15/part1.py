#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().split(",")


def get_hash(line):
    hash_value = 0
    for x in line:
        hash_value += ord(x)
        hash_value *= 17
        hash_value %= 256
    return hash_value


print(sum([get_hash(x) for x in lines]))
