#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


#
# Complete the 'reverseBetween' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER left
#  3. INTEGER right
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverseBetween(head, left, right):
    # Write your code here
    if not head:
        return head

    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    prev = dummy

    # Move `prev` to the node before `left`
    for _ in range(left - 1):
        prev = prev.next

    # `start` will point to the node at position `left`
    start = prev.next
    then = start.next

    # Reverse the nodes between `left` and `right`
    for _ in range(right - left):
        start.next = then.next
        then.next = prev.next
        prev.next = then
        then = start.next

    return dummy.next
    
    
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    left = int(input().strip())

    right = int(input().strip())

    result = reverseBetween(head.head, left, right)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()
