#!/usr/bin/env python3
from itertools import cycle

data = open('21.txt', 'r').read().strip().split("\n")

positions = []
for line in data:
    num = int(line.split()[-1].strip())
    positions.append(num)

def part_one(positions: list[int]):
    scores = [0, 0]

    die = cycle(range(1, 101)).__next__
    turn = 0
    rolls = 0

    while max(scores) < 1000:
        for _ in range(3):
            rolls += 1
            positions[turn] = (positions[turn] + die()) % 10
        scores[turn] += positions[turn]

        # update conditions for next round
        turn = not turn

    return scores[turn] * rolls

print(part_one(positions))
