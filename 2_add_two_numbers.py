# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummyNode = curr = ListNode()     
        remainder = 0        
       
        while l1 or l2 or remainder:
            
            # values at each pointer
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            #store their sum
            total = num1 + num2 + remainder
            singleDigitTotal = total % 10

            remainder = total // 10 
            curr.next = ListNode(singleDigitTotal)
            
            # Repeat with next nodes
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummyNode.next