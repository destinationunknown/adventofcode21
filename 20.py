#!/usr/bin/env python3
from collections import defaultdict

data = open('20.txt', 'r').read().strip().split("\n")

# test data
# data = [
#     "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
#     "\n",
#     "#..#."
#     "#....",
#     "##..#",
#     "..#..",
#     "..###"
# ]

algorithm = data[0]

binarize = lambda pattern: [1 if char == "#" else 0 for char in pattern]

algorithm = binarize(algorithm)

image = data[1:]
image = [binarize(line) for line in image if line]

image_dict = defaultdict(int)

for i in range(len(image)):
    for j in range(len(image[i])):
        if image[i][j] == 1:
            image_dict[(i, j)] = 1

image = image_dict

def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return tuple(map(lambda x, y: x + y, a, b))


def get_output_pixel(input_pixel: tuple[int, int], image: dict, algorithm: list[int]) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    output_pixel_index = 0

    s = ""
    for dir in directions:
        s += str(image[add(dir, input_pixel)])

    output_pixel_index = int(s, 2)

    output_pixel = algorithm[output_pixel_index]

    return output_pixel



def apply_algorithm(algorithm: list[int], image: dict, num_steps) -> int:
    for step in range(num_steps):
        # there is a special case if the first character of the algorithm is 1 and the last character is 0
        # essentially empty regions of the image will be toggled between 1 and 0 each iteration of the algorithm
        if algorithm[0] == 1 and algorithm[511] == 0 and step % 2 == 0:
            next_image = defaultdict(lambda: 1)
        else:
            next_image = defaultdict(int)

        min_x = min(x for _, x in image)
        max_x = max(x for _, x in image)
        min_y = min(y for y, _ in image)
        max_y = max(y for y, _ in image)


        for i in range(min_y - 1, max_y + 2):
            for j in range(min_x - 1, max_x + 2):
                output_pixel = get_output_pixel((i, j), image, algorithm)
                next_image[(i, j)] = output_pixel

        image = next_image

    return sum(image.values())

def part_one(algorithm, image):
    return apply_algorithm(algorithm, image.copy(), 2)

def part_two(algorithm, image) -> int:
    return apply_algorithm(algorithm, image.copy(), 50)

print(part_one(algorithm, image))
print(part_two(algorithm, image))
