# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
             #1 steps ahead
        if not head:
            return None

        slowp = head
        fastp = head

        while (fastp and fastp.next):
            slowp = slowp.next
            fastp = fastp.next.next
            if (fastp == slowp):
                return True
            
            # elif (fastp != slowp):
            #     # print(fastp.val, slowp.val)
            #     slowp = slowp.next
            #     fastp = fastp.next.next
        return False
                
                





        