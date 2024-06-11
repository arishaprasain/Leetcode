# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Empty list condition
        if not head:
            return True

        stack = []
        currents = currentl = head

        #Append to stack
        while(currentl):
            stack.append(currentl)
            currentl = currentl.next

        # Point 'currents' to the top of the stack and 'currentl'  to the start of linked list
        currents = stack[-1]
        currentl = head
        
        #Check whether popped element from stack and current element from linked list are same
        while(currentl and currents and stack):
            if currentl.val == currents.val:

                #Increment both pointers
                currentl = currentl.next
                stack.pop()
                if stack:
                    currents = stack[-1]

            else:
                return False
            
        return True
        