#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

def univalCheck(node, val):
    if not node:
        return 1
    elif node.data == val:
        return univalCheck(node.left, val) and univalCheck(node.right, val)
    return 0

def univalTotal(node):
    if not node:
        return 0
    total = univalCheck(node, node.data)
    total += univalTotal(node.left) + univalTotal(node.right)
    return total

if __name__ == '__main__':
    node = Node(0)
    node.left = Node(1)
    node.right = Node(0)
    node.right.left = Node(1)
    node.right.left.left = Node(1)
    node.right.left.right = Node(1)
    node.right.right = Node(0)
    print(univalTotal(node))

    node = Node(1)
    node.left = Node(3)
    node.right = Node(2)
    node.right.left = Node(2)
    node.right.right = Node(2)
    node.right.right.right = Node(2)
    print(univalTotal(node))

    node = Node(5)
    node.left = Node(1)
    node.left.left = Node(5)
    node.left.right = Node(5)
    node.right = Node(5)
    node.right.right = Node(5)
    print(univalTotal(node))
