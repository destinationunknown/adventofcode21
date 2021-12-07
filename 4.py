#!/usr/bin/env python3

data = open('4.txt', 'r').read().strip().split('\n')

# Get the list of bingo numbers
nums = list(map(int, data[0].split(',')))
data = data[1:]
# trim newlines
data = [x for x in data if x]

def get_boards():
    """Generate the list of boards from the data"""
    boards = []
    for i in range(0, len(data), 5):
        curr_board = []
        for j in range(i, i + 5):
            curr_line = []
            for x in data[j].split(' '):
                if x:
                    curr_line.append(int(x.strip()))
            curr_board.append(curr_line)

        boards.append(curr_board)
    return boards


def check_board(board) -> int:
    """
    take in a board, and return the "score" of that board

    if the board is not yet complete, the score will be 0

    if the board is complete, then the score is the sum of all unmarked numbers on the board

    positions that are 'marked' are set to -1
    """
    rows = [True] * 5
    cols = [True] * 5

    score = 0

    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem != -1:
                rows[i] = False
                cols[j] = False
                score += elem

    if any(rows) or any(cols):
        return score
    else:
        return 0

def update_board(board, num):
    """
    Update the board to mark the current number in the board
    """
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem == num:
                board[i][j] = -1
    

def part_one():
    boards = get_boards()
    for num in nums:
        for board in boards:
            update_board(board, num)
            res = check_board(board)
            if res > 0:
                return res * num


def part_two():
    boards = get_boards()
    for num in nums:
        for i in range(len(boards) - 1, -1, -1,):
            board = boards[i]
            update_board(board, num)
            res = check_board(board)
            if res > 0:
                if len(boards) == 1:
                    return res * num
                else:
                    del boards[i]


print(part_one())
print(part_two())
