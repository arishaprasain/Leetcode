# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slowp = fastp = head
        if not head or not head.next:
            return None
        while(fastp and fastp.next):
            slowp = slowp.next
            fastp = fastp.next.next
           
            
            if (slowp == fastp):
                # cycle is detected
                slowp = head
                while (slowp != fastp):
                    slowp = slowp.next
                    fastp = fastp.next
                return slowp
    
        