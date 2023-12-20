#!/usr/bin/env python3

with open('input.txt') as f:
    parts = f.read().split("\n\n")

workflows = parts[0].splitlines()

data = [x[1:-1] for x in parts[1].splitlines()]
ratings = [dict(entry.split("=") for entry in line.split(",")) for line in data]

instructions = {}
for workflow in workflows:
    label, rules = workflow[:-1].split("{")
    instructions[label] = rules


def evaluate(next_step, current_ratings):
    predicate = next_step.split(":", 1)[0]
    greater = ">" in predicate
    var, rest = next_step.split(">", 1) if greater else next_step.split("<", 1)
    val, next = rest.split(":", 1)
    index = 0 if (
        int(current_ratings.get(var)) > int(val) if greater else int(current_ratings.get(var)) < int(val)) else 1
    next = next.split(",", 1)[index]
    if ":" in next:
        return evaluate(next, current_ratings)
    else:
        return run_program(next, current_ratings)


def run_program(instruction, current_ratings):
    if instruction in ("A", "R"):
        return instruction == 'A'
    else:
        next_step = instructions.get(instruction)
        return evaluate(next_step, current_ratings)


result = [sum([int(x) for x in rating.values()]) if run_program("in", rating) else 0 for rating in ratings]
print(sum(result))
