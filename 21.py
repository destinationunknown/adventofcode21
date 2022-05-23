#!/usr/bin/env python3

data = open('21.txt', 'r').read().strip().split("\n")
positions = []
for line in data:
    num = int(line.split()[-1].strip())
    positions.append(num)

def inc(num: int, start: int, threshold: int):
    if num == threshold:
        return start
    else:
        return num + 1

def part_one(positions: list[int]):
    # we will offset the positions by 1 to make modulus logic easier
    positions = [pos - 1 for pos in positions]
    scores = [0, 0]

    die = 0
    turn = 0
    rolls = 0

    while max(scores) < 1000:
        for _ in range(3):
            die = inc(die, start=1, threshold=100)
            rolls += 1
            positions[turn] = (positions[turn] + die) % 10
        scores[turn] += (positions[turn] + 1)

        # update conditions for next round
        turn = inc(turn, 0, 1)

    return scores[turn] * rolls

print(part_one(positions))
