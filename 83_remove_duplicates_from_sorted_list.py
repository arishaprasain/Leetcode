# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):

        """
        :type head: ListNode
        :rtype: ListNode
        """
  
        ptr1 = head
        

        if not head:
            return None

        while(ptr1 and ptr1.next):
            if (ptr1.val == ptr1.next.val):            
                
               
                ptr1.next = ptr1.next.next

            else :
                ptr1 = ptr1.next
                ptr1.next = ptr1.next

        
        return head
        