# Definition for singly-linked list.
# Temp head approach
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Empty condition
        if not head or not head.next:
            return head

        current = head
        ptr = head.next
        dummy = prev = ListNode(0, head)

        while(current and current.next):
            #nodes
            first = current
            second = current.next
            third = second.next
        
            #Connecting nodes and swapping
            prev.next = second
            first.next = third
            second.next  = first
            
            #Incrementing pointer
            prev = first
            current = first.next


        return dummy.next





        