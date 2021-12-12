#!/usr/bin/env python3

data = open('6.txt', 'r').read().strip().split('\n')
data = list(map(int, data[0].split(',')))
# data = [3,4,3,1,2]
# DAYS = 18

# we will keep track of all fish by internal timer
def count_fish(days):
    fish = [0] * 9

    # initialize array
    for num in data:
        fish[num] += 1

    # every day, we want to update the fish buckets
    # the fish in bucket n will move to bucket n - 1 as their internal timer decreases by 1
    # the fish in bucket 0 will move to bucket 6
    # they will also create new fish in bucket 8
    #
    for day in range(days):
        bucket_0 = fish[0]
        for i in range(len(fish) - 1):
            fish[i] = fish[i + 1]
        fish[6] += bucket_0
        fish[8] = bucket_0

    return sum(fish)


def part_one():
    return count_fish(80)

def part_two():
    return count_fish(256)

print(part_one())
print(part_two())
