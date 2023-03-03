#!/usr/bin/env python3
import pdb

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if (not root):
        return '-1'
    string = str(root.val)
    string = string + ' ' + serialize(root.left)
    string = string + ' ' + serialize(root.right)
    return string

def _deserialize(li):
    node = Node('')
    if (not li or not li[0]):
        return
    if (li[0] == '-1'):
        li.pop(0)
        return
    node.val = li[0]
    li.pop(0)
    node.left = _deserialize(li)
    node.right = _deserialize(li)
    return node
    
def deserialize(s):
    return _deserialize(s.split(sep=" "))

#test code

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
