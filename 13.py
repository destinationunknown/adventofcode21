#!/usr/bin/env python3

data = open('13.txt', 'r').read().strip().split('\n')

data = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5"
]

split = data.index("")

coords = data[:split]
coords = [tuple(map(int, line.split(','))) for line in coords]
folds = data[split+1:]
folds = [(line[11], int(line[13:])) for line in folds]

print(folds)

def part_one():
    pass

def part_two():
    pass

print(part_one())
print(part_two())
