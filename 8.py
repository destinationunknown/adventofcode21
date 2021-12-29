#!/usr/bin/env python3

data = open('8.txt', 'r').read().strip().split('\n')
# data = [
#     "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
#     "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
#     "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
#     "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
#     "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
#     "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
#     "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
#     "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
#     "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
#     "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
# ]
data = [[x.strip().split(" ") for x in line.split('|')] for line in data]

def part_one(data):
    res = 0
    for line in data:
        in_segments, out_segments = line
        res += len(list(filter(lambda x: len(x) in (2, 3, 4, 7), out_segments)))
    return res

def part_two(data):
    res = 0

    for line in data:
        in_segments, out_segments = line
        # Using frozenset because it can be used as a key for a dict
        in_segments = [frozenset(list(segment)) for segment in in_segments]
        # Put the combinations we know at the front
        in_segments = list(sorted(in_segments, key=lambda x: len(x) not in (2, 3, 4, 7)))
        out_segments = [frozenset(list(segment)) for segment in out_segments]

        # If we know 1 and 4, we can figure out the rest
        # We basically need to find a unique identifier for each combination of segments
        # 1, 4, 7, 8 have a unique number of segments
        known_lens = {
            2: 1,
            3: 7,
            4: 4,
            7: 8
        }
        unique_nums = {}
        known_nums = {}
        for segment in in_segments:
            if segment not in known_nums:
                if len(segment) in known_lens:
                    unique_nums[known_lens[len(segment)]] = segment
                    known_nums[segment] = known_lens[len(segment)]
                else:
                    # We need to figure these out using the known segment sets (sets with unique lengths)
                    # length 6: 0, 6, 9
                    # if 1's set is not in the set, then it is 6
                    # if 4's set is in the set, then it is 9
                    # else, it is 0
                    if len(segment) == 6:
                        if not unique_nums[1].issubset(segment):
                            known_nums[segment] = 6
                        elif unique_nums[4].issubset(segment):
                            known_nums[segment] = 9
                        else:
                            known_nums[segment] = 0

                    # length 5: 2, 3, 5
                    # if 1's set is in the set, then it is 3
                    # if (8's set - 4's set) is in the set, then it is 2
                    if len(segment) == 5:
                        if unique_nums[1].issubset(segment):
                            known_nums[segment] = 3
                        elif (unique_nums[8] - unique_nums[4]).issubset(segment):
                            known_nums[segment] = 2
                        else:
                            known_nums[segment] = 5

        cur_sum = 0
        ten_pow = 1
        for segment in list(reversed(out_segments)):
            cur_sum += known_nums[segment] * ten_pow
            ten_pow *= 10

        res += cur_sum

    return res

print(part_one(data))
print(part_two(data))
