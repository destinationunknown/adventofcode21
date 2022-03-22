#!/usr/bin/env python3
from collections import defaultdict, Counter

data = open('14.txt', 'r').read().strip().split('\n')

# Test data:
# data = [
#     "NNCB",
#     "\n",
#     "CH -> B",
#     "HH -> N",
#     "CB -> H",
#     "NH -> C",
#     "HB -> C",
#     "HC -> B",
#     "HN -> C",
#     "NN -> C",
#     "BH -> H",
#     "NC -> B",
#     "NB -> B",
#     "BN -> B",
#     "BB -> N",
#     "BC -> B",
#     "CC -> N",
#     "CN -> C"
# ]

polymer = data[0]
rules_text = data[2:]

rules = {}
for line in data[2:]:
    key, val = [x.strip() for x in line.split("->")]
    rules[key] = val

def update_polymer_brute_force(polymer: list, rules: dict, num_steps):
    for step in range(num_steps):
        i = 0
        while i < len(polymer) - 1:
            section = "".join(polymer[i:i+2])
            if section in rules:
                i += 1
                polymer.insert(i, rules[section])
            i += 1


    counts = [x[1] for x in Counter(polymer).most_common()]
    return counts[0] - counts[-1]

def update_polymer(polymer: str, rules: dict, num_steps: int):
    # initialize pairs
    pairs = defaultdict(int)
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        pairs[pair] += 1


    for step in range(num_steps):
        next_pairs = defaultdict(int)
        for pair in pairs:
            next_pairs[pair[0] + rules[pair]] += pairs[pair]
            next_pairs[rules[pair] + pair[1]] += pairs[pair]

        pairs = next_pairs



    # go from pair count to actual letter count
    # the same char will be the first part of one pair and the second part of another pair
    count_first = defaultdict(int)
    count_last = defaultdict(int)
    count = {}
    letters = rules.values()


    for pair in pairs:
        pair_count = pairs[pair]
        count_first[pair[0]] += pair_count
        count_last[pair[1]] += pair_count

    for letter in letters:
        # don't double count letters
        count[letter] = max(count_first[letter], count_last[letter])

    return max(count.values()) - min(count.values())

def part_one(polymer, rules):
    return update_polymer(polymer, rules, 10)

def part_two(polymer, rules):
    return update_polymer(polymer, rules, 40)

print(part_one(polymer, rules))
print(part_two(polymer, rules))
