data = open('1.txt', 'r').read().split('\n')

def part_one():
    prev = 0
    count = 0

    for line in data:
        if len(line) > 0:
            num = int(line)
            if num > prev:
                count += 1
            prev = num

    print(count - 1)

def part_two():
    a = int(data[0])
    b = int(data[1])
    cur_sum = a + b
    prev_sum = 0
    count = 0

    for line in data[2:]:
        if len(line) > 0:
            c = int(line)
            cur_sum += c
            if cur_sum > prev_sum:
                count += 1
            prev_sum = cur_sum
            cur_sum -= a
            a = b
            b = c

    print(count - 1)

part_one()
part_two()
