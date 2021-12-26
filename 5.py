#!/usr/bin/env python3
import math

data = open('5.txt', 'r').read().strip().split('\n')

lines = []
for line in data:
    if line:
        line = line.split('->')
        lines.append(tuple(tuple(map(int, pair.strip().split(","))) for pair in line))

SIZE = 1000

def part_one():
    """Brute force solution"""
    matrix = [[0] * SIZE for i in range(SIZE)]
    count = 0

    for line in lines:
        # since the lines are either vertical or horizontal we can just sort the coordinates individually
        y_coords = sorted((line[0][1], line[1][1]))
        x_coords = sorted((line[0][0], line[1][0]))

        if y_coords[0] == y_coords[1] or x_coords[0] == x_coords[1]:
            for i in range(y_coords[0], y_coords[1] + 1):
                for j in range(x_coords[0], x_coords[1] + 1):
                    matrix[i][j] += 1
    for row in matrix:
        for elem in row:
            if elem >= 2:
                count += 1


    return count

def part_two():
    """Brute force solution"""
    matrix = [[0] * SIZE for i in range(SIZE)]
    count = 0

    for line in lines:
        y_coords = sorted((line[0][1], line[1][1]))
        x_coords = sorted((line[0][0], line[1][0]))

        # line is vertical or horizontal
        if y_coords[0] == y_coords[1] or x_coords[0] == x_coords[1]:
            for i in range(y_coords[0], y_coords[1] + 1):
                for j in range(x_coords[0], x_coords[1] + 1):
                    matrix[i][j] += 1
        else:
            # sort the coordinates by y value
            # two cases, going left or going right
            # line is diagonal, compute distance
            (a, b) = tuple(sorted(line, key=lambda x: x[1]))
            length = int(math.sqrt((y_coords[1] - y_coords[0]) ** 2 + (x_coords[1] - x_coords[1]) ** 2))
            if a[0] > b[0]:
                # line is going down and left
                dir = -1
            else:
                # line is going down and right
                dir = 1

            for i in range(length + 1):
                matrix[a[1] + i][a[0] + (dir * i)] += 1

    for row in matrix:
        for elem in row:
            if elem >= 2:
                count += 1

    return count


print(part_one())
print(part_two())
