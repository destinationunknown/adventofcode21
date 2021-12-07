#!/usr/bin/env python3

data = open('3.txt', 'r').read().strip().split('\n')

def part_one():
    # length of each string
    n = 12
    ones = [0] * n
    num_lines = 0

    for line in data:
        if len(line) > 0:
            num_lines += 1
            num = list(map(int, line))
            for i in range(n):
                ones[i] += int(num[i])

    gamma = 0
    epsilon = 0

    two_pow = 1
    for i in range(n - 1, 0-1, -1):
        if ones[i] > (num_lines // 2):
            gamma += two_pow
        else:
            epsilon += two_pow
        two_pow *= 2


    return gamma * epsilon


def part_two():
    n = 12
    nums = [int(x, 2) for x in data if len(x) > 0]
    two_pow = pow(2, n-1)
    for i in range(n):
        #compute most common bit in this position
        ones = 0
        zeros = 0
        nums_ones = []
        nums_zeros = []

        for num in nums:
            if num & two_pow == two_pow:
                ones += 1
                nums_ones.append(num)
            else:
                zeros += 1
                nums_zeros.append(num)

        if ones >= zeros:
            nums = nums_ones
        else:
            nums = nums_zeros

        two_pow //= 2

    oxygen = nums[0]

    nums = [int(x, 2) for x in data if len(x) > 0]
    two_pow = pow(2, n-1)
    for i in range(n):
        #compute least common bit in this position
        ones = 0
        zeros = 0
        nums_ones = []
        nums_zeros = []

        for num in nums:
            if num & two_pow == two_pow:
                ones += 1
                nums_ones.append(num)
            else:
                zeros += 1
                nums_zeros.append(num)

        if ones < zeros:
            nums = nums_ones
        else:
            nums = nums_zeros

        two_pow //= 2
        if len(nums) == 1:
            break

    co2 = nums[0]

    return oxygen * co2

print(part_one())
print(part_two())
