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
# Complete the 'middleNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def middleNode(head):
    # Write your code here
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
      
    current = head  
    #count even
    if (count % 2 == 0):
        index = count/2 + 1
        i = 1
        while i < index:
            i += 1
            current = current.next
        return current
            
             
    elif (count % 2 == 1):
        index = (count + 1)/2
        i = 1
        while i < index:
            i += 1
            current = current.next
        return current
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    result = middleNode(head.head)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()
