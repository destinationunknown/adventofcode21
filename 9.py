#!/usr/bin/env python3

from functools import reduce


data = open('9.txt', 'r').read().strip().split('\n')

# data = [
#     "2199943210",
#     "3987894921",
#     "9856789892",
#     "8767896789",
#     "9899965678"
# ]

data = [list(map(int, list(line))) for line in data]

def get_low_points(data):
    low_points = {}

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            is_low_point = [False, False, False, False]
            if i == 0 or data[i-1][j] > val:
                is_low_point[0] = True

            if i == len(data) - 1 or data[i + 1][j] > val:
                is_low_point[1] = True

            if j == 0 or data[i][j - 1] > val:
                is_low_point[2] = True

            if j == len(data[i]) - 1 or data[i][j + 1] > val:
                is_low_point[3] = True

            if all(is_low_point):
                low_points[(i, j)] = val + 1

    return low_points

def part_one(data):
    return sum(get_low_points(data).values())

# Explore outwards from a point
def find_basin_size(data, row, col):
    if row >= 0 and row < len(data) and col >= 0 and col < len(data[row]) and data[row][col] != 9:
        data[row][col] = 9
        return 1 + sum([
            find_basin_size(data, row - 1, col),
            find_basin_size(data, row + 1, col),
            find_basin_size(data, row, col - 1),
            find_basin_size(data, row, col + 1)
        ])
    else:
        return 0


def part_two(data):
    # Use all the low points as starting points
    low_points = get_low_points(data).keys()
    basin_sizes = []
    for (row, col) in low_points:
        print(f"low point: {row}, {col}")
        basin_sizes.append(find_basin_size(data, row, col))
        print(f"basin size: {basin_sizes[-1]}")

    basin_sizes.sort(reverse=True)
    return reduce(lambda x, y: x * y, basin_sizes[0:3])


print(part_one(data))
print(part_two(data))
