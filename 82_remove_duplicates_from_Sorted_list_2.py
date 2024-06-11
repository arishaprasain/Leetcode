# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while(current and current.next):
            if (current.next and current.val == current.next.val):
                while(current.next and current.val == current.next.val):
                    current = current.next

                
                prev.next = current.next
                current = current.next

            else:
                prev = current
                current = current.next
                prev.next = current

                 
                
        return dummy.next