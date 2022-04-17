#!/usr/bin/env python3

data = open('16.txt', 'r').read().strip()

# test data
# data = "8A004A801A8002F478"
# data = "D2FE28"
# data = "38006F45291200"
# data = "EE00D40C823060"
# data = "C0015000016115A2E0802F182340"
# data = "8A004A801A8002F478" # 16
# data = "620080001611562C8802118E34"

# global variable to store sum of all version numbers
global version_sum
version_sum = 0

# main idea: parse the packets into a tree-like structure with packets and subpackets
class Packet:
    version: int
    type_id: int
    length_type_id: int
    value: int
    num_subpackets: int
    len_subpackets: int
    subpackets: list

    # Initialize a packet from a bit string
    def parse(self, bit_string: str, start: int) -> int:
        curr = start
        # first 3 bits are the version
        self.version = int(bit_string[curr:curr+3], base=2)
        global version_sum
        version_sum += self.version
        curr += 3
        # next 3 bits are the type id
        self.type_id = int(bit_string[curr:curr+3], base=2)
        curr += 3

        if self.type_id == 4:
            # literal packet, contains a single binary value
            # split into groups of 5 bits, with the first bit denoting the group type and the next 4 containing the group's value
            # groups starting with 1 are non-terminating
            # groups starting with 0 are the last group
            # there may be trailing 0s after the last group
            value_str = ""

            read_last = False
            while not read_last and bit_string[curr]:
                if bit_string[curr] == "0":
                    read_last = True

                curr += 1
                value_str += bit_string[curr:curr+4]
                curr += 4

            # get actual value from binary string
            self.value = int(value_str, base=2)

        else:
            # operator packet
            self.length_type_id = int(bit_string[curr], base=2)
            curr += 1

            self.subpackets = []
            if self.length_type_id == 0:
                # value of next 15 bits is the length of subpackets
                self.len_subpackets = int(bit_string[curr:curr+15], base=2)
                curr += 15

                # parse remaining subpackets
                end = curr + self.len_subpackets
                while curr < end:
                    subpacket = Packet()
                    curr = subpacket.parse(bit_string, start=curr)
                    self.subpackets.append(subpacket)
            else:
                # value of next 11 bits is the number of subpackets
                self.num_subpackets = int(bit_string[curr:curr+11], base=2)
                curr += 11

                # parse remaining subpackets
                for i in range(self.num_subpackets):
                    subpacket = Packet()
                    curr = subpacket.parse(bit_string, start=curr)
                    self.subpackets.append(subpacket)

        return curr

def get_bit_string(data: str) -> str:
    bits = ''
    for x in data:
        bits += str(bin(int(x,16)))[2:].zfill(4)
    return bits

def part_one(data):
    bit_string = get_bit_string(data)
    root = Packet()
    root.parse(bit_string, start=0)
    return version_sum


print(part_one(data))
