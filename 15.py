#!/usr/bin/env python3

import heapq
from collections import defaultdict
import numpy as np

data = open('15.txt', 'r').read().strip().split('\n')

# test data
# data = [
#     "1163751742",
#     "1381373672",
#     "2136511328",
#     "3694931569",
#     "7463417111",
#     "1319128137",
#     "1359912421",
#     "3125421639",
#     "1293138521",
#     "2311944581"
# ]

grid = [[int(x) for x in list(line)] for line in data]

def dijkstras(grid: list) -> int:
    dist = defaultdict(lambda: float("inf"))
    dist[(0, 0)] = 0
    goal = (len(grid) - 1, len(grid[0]) - 1)
    q = []
    heapq.heappush(q, (0, (0, 0)))
    visited = set()

    def is_valid(pos):
        row, col = pos
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row])

    def get_neighbours(pos):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbours = [tuple(sum(x) for x in zip(pos, d)) for d in dirs]
        valid_neighbours = [n for n in neighbours if is_valid(n)]
        return valid_neighbours

    while q:
        _, pos = heapq.heappop(q)
        row, col = pos
        visited.add(pos)

        for neighbour in get_neighbours(pos):
            if neighbour in visited:
                continue

            n_row, n_col = neighbour
            cost = grid[n_row][n_col]

            new_dist = dist[pos] + cost
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                # would update prev here if we needed to
                heapq.heappush(q, (new_dist, neighbour))


    return dist[goal]

def part_one(grid: list):
    return dijkstras(grid)

def part_two(grid: list):
    grid = np.asarray(grid)
    tiled_grid = np.tile(grid, (5, 5))
    for i in range(5):
        for j in range(5):
            tiled_grid[len(grid) * i:len(grid) * (i + 1), len(grid[0]) * j : len(grid[0]) * (j + 1)] += (i + j)

    # Values wrap around to 1, not 0
    tiled_grid[tiled_grid > 9] += 1
    tiled_grid = tiled_grid % 10

    return dijkstras(tiled_grid)


print(part_one(grid))
print(part_two(grid))
