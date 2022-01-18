#!/usr/bin/env python3
from collections import defaultdict

data = open('12.txt', 'r').read().strip().split('\n')

# Test data
# data = [
#     "start-A",
#     "start-b",
#     "A-c",
#     "A-b",
#     "b-d",
#     "A-end",
#     "b-end"
# ]

# Generate graph structure from input
caves = defaultdict(list)
for line in data:
    x, y = line.split("-")
    caves[x].append(y)
    caves[y].append(x)

def part_one_helper(caves: dict, curr: str, visited: set) -> int:
    """
    Return the number of paths from the current node to the end node.
    We don't have to worry about infinite loops because there are never two big caves connected to each other.
    """

    if curr == "end":
        return 1

    visited = set.copy(visited)
    if curr.islower():
        visited.add(curr)

    paths = 0

    for neighbour in caves[curr]:
        if neighbour not in visited:
            paths += part_one_helper(caves, neighbour, visited)

    return paths

def part_one(caves):
    visited = set()
    return part_one_helper(caves, "start", visited)


def part_two_helper(caves: dict, curr: str, visited: set, visited_twice: bool) -> int:
    """
    If the visited_twice string is empty and the current cave is a small cave, we have two choices:
    1. Choose to visit the current cave twice. Set the visited_twice string and don't add the current cave to the visited set.
    2. Visit another future cave twice. Add the current cave to the visited set as normal.

    If the string is not empty (we have already decided to use a certain cave twice on this path),
    we change the string to USED when it is used for the second time.
    """
    if curr == "end":
        return 1

    paths = 0

    visited = set.copy(visited)
    if curr.islower():
        visited.add(curr)

    for neighbour in caves[curr]:
        if neighbour not in visited:
            paths += part_two_helper(caves, neighbour, visited, visited_twice)
        elif neighbour in visited and neighbour != "start" and not visited_twice:
            paths += part_two_helper(caves, neighbour, visited, True)

    return paths

def part_two(caves):
    visited = set()
    return part_two_helper(caves, "start", visited, False)

print(part_one(caves))
print(part_two(caves))
