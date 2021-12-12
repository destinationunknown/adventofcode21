#!/usr/bin/env python3
from statistics import mean, median

data = open('7.txt', 'r').read().strip().split('\n')
data = list(map(int, data[0].split(',')))

def part_one(data):
    pos = int(median(data))
    fuel = 0
    for crab in data:
        fuel += abs(pos - crab)
    return fuel

def part_two(data):
    # using mean seemed plausible but doesn't give the right answer
    # instead we'll use brute force, computing the cost for all possible positions
    # sum from 1 to n is n(n+1)/2
    fuel_cost = lambda crab, pos: abs(pos - crab) * (abs(pos - crab) + 1) // 2
    fuel = float("inf")
    start, end = min(data), max(data)
    for pos in range(start, end + 1):
        fuel = min(fuel, sum([fuel_cost(crab, pos) for crab in data]))

    return fuel

print(part_one(data))
print(part_two(data))
