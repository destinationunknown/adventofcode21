#!/usr/bin/env python3
import itertools
from collections import deque

data = open('11.txt', 'r').read().strip().split('\n')

# # Example input
# data = [
#     "5483143223",
#     "2745854711",
#     "5264556173",
#     "6141336146",
#     "6357385478",
#     "4167524645",
#     "2176841721",
#     "6882881134",
#     "4846848554",
#     "5283751526"
# ]

# data = [
#    "11111",
#    "19991",
#    "19191",
#    "19991",
#    "11111",
# ]

data = [list(map(int, list(line))) for line in data]

def valid_neighbours(data, point):
   """
   Return a list of all the valid neighbours of a point
   """
   directions = list(itertools.product((0, -1, 1), repeat=2))
   directions.remove((0, 0))
   points = []
   (row, col) = point

   for row_shift, col_shift in directions:
      new_row = row + row_shift
      new_col = col + col_shift
      if new_row in range(0, len(data)) and new_col in range(len(data[row])):
         points.append((new_row, new_col))

   return points


def to_flash(data, flashed):
   """
   Return all coordinates that are to be flashed (value > 9).
   Exclude coordinates that have already been flashed.
   """
   coords = []
   for i, row in enumerate(data):
      for j, value in enumerate(row):
         if value > 9 and (point := (i, j)) not in flashed:
            coords.append(point)

   return coords

def flash(data, coords):
   """
   Flash a set of points
   Set their values to 0, and increase neighbouring values by 1
   """
   flashed = []
   for point in coords:
      flashed.append(point)
      row, col = point
      neighbours = valid_neighbours(row, col)

   return flashed


def part_one(data):
   flash_count = 0
   for step in range(1, 101):
      flashed = set()
      stack = deque()
      # First, increase the brightness of every octopus by 1
      for row in range(len(data)):
         for col in range(len(data[row])):
               data[row][col] += 1
               if data[row][col] > 9:
                  stack.append((row, col))

      # continue as long as there are still octopuses to flash
      while len(stack) > 0:
         # flash the point, setting its value to 0 and increasing neighbours by 1
         curr = stack.pop()
         # neighbours are only increased by 1 if the point has not already flashed
         if curr not in flashed:
            data[curr[0]][curr[1]] = 0
            flashed.add(curr)
            neighbours = valid_neighbours(data, curr)
            for (row, col) in neighbours:
               if (row, col) not in stack and (row, col) not in flashed:
                  data[row][col] += 1
                  if data[row][col] > 9:
                     stack.append((row, col))

      flash_count += len(flashed)

   return flash_count



def part_two(data):
   step = 101
   while True:
      flashed = set()
      stack = deque()
      # First, increase the brightness of every octopus by 1
      for row in range(len(data)):
         for col in range(len(data[row])):
               data[row][col] += 1
               if data[row][col] > 9:
                  stack.append((row, col))

      # continue as long as there are still octopuses to flash
      while len(stack) > 0:
         # flash the point, setting its value to 0 and increasing neighbours by 1
         curr = stack.pop()
         # neighbours are only increased by 1 if the point has not already flashed
         if curr not in flashed:
            data[curr[0]][curr[1]] = 0
            flashed.add(curr)
            neighbours = valid_neighbours(data, curr)
            for (row, col) in neighbours:
               if (row, col) not in stack and (row, col) not in flashed:
                  data[row][col] += 1
                  if data[row][col] > 9:
                     stack.append((row, col))

      print(data)
      finished = True
      for row in data:
         for val in row:
            if val != 0:
               finished = False
      if finished:
         return step
      else:
         step += 1


print(part_one(data))
print(part_two(data))
