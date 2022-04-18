#!/usr/bin/env python3

data = open('17.txt', 'r').read().strip()
# data = "target area: x=20..30, y=-10..-5"
_, _, target_xs, target_ys = data.split()
target_xs = [int(x) for x in target_xs[2:-1].split("..")]
target_ys = [int(y) for y in target_ys[2:].split("..")]

target_x_min, target_x_max = target_xs
target_y_min, target_y_max = target_ys


# Note: it is assumed that the target area is always below the start position
# this is true in the puzzle examples and the puzzle input

def probe(data):
    count = 0
    x_min = 1
    x_max = target_x_max
    y_min = target_y_min
    # TODO: comment why this works
    y_max = abs(target_y_min)

    y_pos_max = 0

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            vx, vy = x, y
            x_pos, y_pos = 0, 0

            # highest y reached in this x,y combination
            # tracking this separately because this x,y may not necessarily hit target area
            y_curr_pos_max = 0

            # TODO: comment why this is the range for t
            for t in range(2 * y_max + 2):
                x_pos += vx
                y_pos += vy
                y_curr_pos_max = max(y_curr_pos_max, y_pos)
                vx = max(vx - 1, 0)
                vy -= 1

                if x_pos in range(target_x_min, target_x_max + 1) and y_pos in range(target_y_min, target_y_max + 1):
                    y_pos_max = max(y_pos_max, y_curr_pos_max)
                    count += 1
                    break


    return y_pos_max, count


def part_one(data):
    return probe(data)[0]

def part_two(data):
    return probe(data)[1]

print(part_one(data))
print(part_two(data))
