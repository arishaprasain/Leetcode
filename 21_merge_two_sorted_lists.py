# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #temporary head
        prev = dummy = ListNode()


        if not list1 and not list2:
            return list1

        if list1 and not list2:
            return list1

        if list2 and not list1:
            return list2  

        current = prev
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                prev = current
                current = current.next
                
            else:
                current.next = list2
                list2 = list2.next
                prev = current
                current = current.next
                # print("else loop")
                # print(current.val)
                
        if list1:
            current.next = list1
        else:
            current.next = list2

        
            
        return dummy.next