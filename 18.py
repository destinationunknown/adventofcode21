#!/usr/bin/env python3
from __future__ import annotations
from ast import literal_eval
from typing import Union
from itertools import permutations

data = open('18.txt', 'r').read().strip().split("\n")

# data = [
#     "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
#     "[[[5,[2,8]],4],[5,[[9,9],0]]]",
#     "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
#     "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
#     "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
#     "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
#     "[[[[5,4],[7,7]],8],[[8,3],8]]",
#     "[[9,3],[[9,9],[6,[4,9]]]]",
#     "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
#     "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
# ]

# data = [
#     "[[[[4,3],4],4],[7,[[8,4],9]]]",
#     "[1,1]"
# ]


data = [literal_eval(line) for line in data]

class TreeNode:
    left: Union[TreeNode, None]
    right: Union[TreeNode, None]
    parent: Union[TreeNode, None]
    value: int

    def __init__(self):
        self.left = None
        self.right = None
        self.value = 0
        self.parent = None

    def __repr__(self):
        return tree_to_string(self)

def tree_to_string(node, highlight=None):
    if not (node.left and node.right):
        return '*' + str(node.value) + '*' if node == highlight else str(node.value)
    return ('*[*' if node == highlight else '[') + tree_to_string(node.left, highlight) + ',' + tree_to_string(node.right, highlight) + ']'

def make_tree(data) -> TreeNode:
    node = TreeNode()
    if type(data) == list:
        node.left = make_tree(data[0])
        node.right = make_tree(data[1])

        node.left.parent = node
        node.right.parent = node
    else:
        node.value = int(data)

    return node

def is_leaf(node: TreeNode) -> bool:
    return node.left == None and node.right == None


def explode(node: TreeNode):
    node_to_explode = get_node_to_explode(node, 4)

    if node_to_explode == None:
        return False

    left = get_left_num(node_to_explode.left)
    if left and node_to_explode.left:
        left.value += node_to_explode.left.value

    right = get_right_num(node_to_explode.right)
    if right and node_to_explode.right:
        right.value += node_to_explode.right.value

    node_to_explode.left = None
    node_to_explode.right = None
    node_to_explode.value = 0

    return True

def get_node_to_explode(node: TreeNode, depth=4) -> Union[TreeNode, None]:
    if depth == 0 and not is_leaf(node):
        return node

    if node.left:
        left = get_node_to_explode(node.left, depth - 1)
        if left != None:
            return left
    if node.right:
        right = get_node_to_explode(node.right, depth - 1)
        if right:
            return right
    else:
        return None

# important note: all actual numbers are always leaf nodes

# get first number to the left of a node
def get_left_num(node):
    # root node cannot have any number to the left
    if node.parent == None:
        return None

    # if it is a left child, we should start looking left from the parent
    if node.parent.left == node:
        return get_left_num(node.parent)

    # if it is a right child, we should start looking right from the left sibling
    left = node.parent.left
    curr = left
    while curr.right:
        curr = curr.right

    return curr

# get first number to the right of a node
def get_right_num(node):
    if node.parent == None:
        return None

    # if it is a right child, we should start looking right from the parent
    if node.parent.right == node:
        return get_right_num(node.parent)

    # if it is a left child, we should start looking left from the right sibling
    right = node.parent.right
    curr = right

    while curr.left:
        curr = curr.left

    return curr

def split(node: TreeNode):
    try:
        if is_leaf(node) and node.value >= 10:
            node.left = TreeNode()
            node.left.value = node.value // 2
            node.left.parent = node

            node.right = TreeNode()
            node.right.value = (node.value + 1) // 2
            node.right.parent = node
            return True
        if node.left:
            did_split_left = split(node.left)
            if did_split_left:
                return True
        if node.right:
            did_split_right = split(node.right)
            if did_split_right:
                return True
        else:
            return False
    except:
        print(f"Error parsing node {node}")

def add(a, b):
    node = TreeNode()
    node.left = a
    node.right = b
    a.parent = node
    b.parent = node
    return node

def magnitude(node: TreeNode) -> int:
    if is_leaf(node):
        return node.value
    else:
        return 3 * magnitude(node.left) + 2 * magnitude(node.right)

def reduce(node):
    while explode(node) or split(node):
        continue

def part_one(data) -> int:
    root = make_tree(data[0])

    for line in data[1:]:
        to_add = make_tree(line)
        root = add(root, to_add)

        reduce(root)

    return magnitude(root)


def part_two(data) -> int:
    ...



print(part_one(data))
print(part_two(data))

def test_magnitude():
    test_cases = [
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488)

    ]

    for test_case in test_cases:
        data, expected_magnitude = test_case
        node = make_tree(literal_eval(data))
        print(expected_magnitude)
        print(type(magnitude(node)))
        assert magnitude(node) == expected_magnitude


def test_explode():
    test_cases = [
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
    ]

    for test_case in test_cases:
        data, expected_tree = test_case
        node = make_tree(literal_eval(data))
        did_explode = explode(node)
        assert did_explode
        assert tree_to_string(node) == expected_tree

def test_add():
    test_cases = [
        (("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"), "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
    ]

    for test_case in test_cases:
        data, expected_tree = test_case
        a, b = data
        a = make_tree(literal_eval(a))
        b = make_tree(literal_eval(b))
        c = add(a, b)
        assert tree_to_string(c) == expected_tree
