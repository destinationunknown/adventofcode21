#!/usr/bin/env python3

data = open('2.txt', 'r').read().split('\n')

def part_one():
    x = 0
    y = 0
    for line in data:
        if len(line) > 0:
            [direction, distance] = line.split(' ')
            if direction == "forward":
                x += int(distance)
            elif direction == "down":
                y += int(distance)
            elif direction == "up":
                y -= int(distance)
    return x * y

def part_two():
    x = 0
    y = 0
    aim = 0
    for line in data:
        if len(line) > 0:
            [direction, distance] = line.split(' ')
            if direction == "forward":
                x += int(distance)
                y += aim * int(distance)
            elif direction == "down":
                aim += int(distance)
            elif direction == "up":
                aim -= int(distance)
    return x * y

print(part_two())
