#!/usr/bin/env python3
data = open('13.txt', 'r').read().strip().split('\n')

# Test data
# data = [
#     "6,10",
#     "0,14",
#     "9,10",
#     "0,3",
#     "10,4",
#     "4,11",
#     "6,0",
#     "6,12",
#     "4,1",
#     "0,13",
#     "10,12",
#     "3,4",
#     "3,0",
#     "8,4",
#     "1,10",
#     "2,14",
#     "8,10",
#     "9,0",
#     "",
#     "fold along y=7",
#     "fold along x=5"
# ]

split = data.index("")

coords = data[:split]
coords = [tuple(map(int, line.split(','))) for line in coords]
coords = set(coords)
folds = data[split+1:]
folds = [(line[11], int(line[13:])) for line in folds]

def print_coords(coords: set):
    max_x = max(x for x, _ in coords)
    max_y = max(y for _, y in coords)

    res = ""

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in coords:
                res += "█"
            else:
                res += " "
        res += "\n"
    return res


def fold(coords: set, fold: tuple):
    folded = set()
    for point in coords:
        if fold[0] == 'y':
            if point[1] > fold[1]:
                folded_y = 2 * fold[1] - point[1]
            else:
                folded_y = point[1]
            folded.add((point[0], folded_y))
        else:
            if point[0] > fold[1]:
                folded_x = 2 *fold[1] - point[0]
            else:
                folded_x = point[0]
            folded.add((folded_x, point[1]))

    return folded


def part_one(coords: set, folds: list) -> int:
    return len(fold(coords, folds[0]))


def part_two(coords: set, folds: list):
    for f in folds:
        coords = fold(coords, f)
    return print_coords(coords)


print(part_one(coords, folds))
print(part_two(coords, folds))
