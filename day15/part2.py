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


boxes = {}

for entry in lines:
    if "=" in entry:
        label, value = entry.split("=")
        hash = get_hash(label)
        lens = [label, value]
        if hash in boxes:
            current_box = boxes[hash]
            founded = False
            for index, items in enumerate(current_box):
                if label == items[0]:
                    founded = True
                    current_box[index] = lens
            if not founded:
                current_box.append(lens)
        else:
            boxes[hash] = [[label, value]]

    elif entry.endswith("-"):
        label = entry[:-1]
        hash = get_hash(label)
        if hash in boxes:
            current_box = boxes[hash]
            for index, items in enumerate(current_box):
                if label == items[0]:
                    del current_box[index]

acc = 0
for key, value in boxes.items():
    if len(value) != 0:
        for index, entry in enumerate(value):
            acc += (1 + int(key)) * (index + 1) * int(entry[1])

print(acc)
