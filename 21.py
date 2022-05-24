#!/usr/bin/env python3

from itertools import cycle, product
from functools import lru_cache
from operator import add

data = open('21.txt', 'r').read().strip().split("\n")

positions = []
for line in data:
    num = int(line.split()[-1].strip())
    positions.append(num)

# positions = [4, 8]

def part_one(positions: list[int]):
    positions = [p for p in positions]
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

all_rolls = tuple(map(sum, product(range(1, 4), range(1, 4), range(1, 4))))

def add_pair(a: tuple[int, int], b: tuple[int, int]):
    return tuple(map(add, a, b))

@lru_cache(maxsize=None)
def part_two_helper(positions: tuple[int, int], scores: tuple[int, int], turn: int = 0) -> tuple[int, int]:
    assert turn in (0, 1)
    if scores[0] >= 21:
        return (1, 0)
    elif scores[1] >= 21:
        return (0, 1)

    wins = (0, 0)

    for roll in all_rolls:
        next_pos = (positions[turn] + roll) % 10
        next_score = scores[turn] + next_pos + 1
        if turn == 0:
            next_positions = (next_pos, positions[1])
            next_scores = (next_score, scores[1])
        else:
            next_positions = (positions[0], next_pos)
            next_scores = (scores[0], next_score)

        other_wins = part_two_helper(next_positions, next_scores, not turn)
        wins = add_pair(wins, other_wins)

    return wins

def part_two(positions: list[int]):
    return max(part_two_helper(tuple([p - 1 for p in positions]), (0, 0), 0))

print(part_one(positions))
print(part_two(positions))
