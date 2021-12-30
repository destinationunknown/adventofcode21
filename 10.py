#!/usr/bin/env python3

from collections import deque

data = open('10.txt', 'r').read().strip().split('\n')
data = [list(line) for line in data]

# data = [
#     "[({(<(())[]>[[{[]{<()<>>",
#     "[(()[<>])]({[<{<<[]>>(",
#     "{([(<{}[<>[]}>{[]{[(<()>",
#     "(((({<>}<{<{<>}{[]{[]{}",
#     "[[<[([]))<([[{}[[()]]]",
#     "[{[{({}]{}}([{[{{{}}([]",
#     "{<[[]]>}<{[{[{[]{()[[[]",
#     "[<(<(<(<{}))><([]([]()",
#     "<{([([[(<>()){}]>(<<{{",
#     "<{([{{}}[<[[[<>{}]]]>[]]",
# ]


pairs = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<': '>'
}

def part_one(data):
    score = 0

    scores = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137,
    }

    for line in data:
        stack = deque()
        for symbol in line:
            if symbol in pairs:
                stack.append(symbol)
            else:
                if symbol == pairs[stack[-1]]:
                    stack.pop()
                else:
                    score += scores[symbol]
                    break

    return score


def part_two(data):
    autocomplete_scores = []

    scores = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4,
    }

    for line in data:
        stack = deque()
        corrupted = False
        for symbol in line:
            if symbol in pairs:
                stack.append(symbol)
            else:
                if symbol == pairs[stack[-1]]:
                    stack.pop()
                else:
                    # Skip this line if it is corrupted
                    corrupted = True
                    break

        # Complete the line
        if not corrupted:
            score = 0
            while len(stack) > 0:
                score *= 5
                score += scores[pairs[stack.pop()]]

            autocomplete_scores.append(score)

    autocomplete_scores.sort()
    return autocomplete_scores[len(autocomplete_scores) // 2]


print(part_one(data))
print(part_two(data))
