# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode                APPROACH ==> 1. Append all the nodes to stack1
                                                         2. Pop n elements from stack1 and push them to stack 2(also identify which node is to be deleted)
                                                         3. Get the node before the node to be deleted
                                                         4. Keep popping nodes from stack2 and  check if it is the node to be deleted and if so skip it
                                                         5. If not, arrange the linked list by manipulating the next pointers and popping from stack2.
        :type n: int
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        current =  head
        index = 0
        while (current is not None):
            stack1.append(current)
            current = current.next

        current = stack1[-1]
        deleted = None
        while (index < n):          
            
            if index == n - 1:
                deleted = stack1.pop()
                stack2.append(deleted)
            
            else :
                stack2.append(stack1.pop())
            index += 1
        
        if not stack1:
            return head.next

        node_before_deleted = stack1[-1]
        # print("Before", node_before_deleted.val)
        new_head = stack1[0]
        while (stack2):
            if stack2[-1] == deleted:
                stack2.pop()
            else:
                node_before_deleted.next = stack2.pop()
                node_before_deleted = node_before_deleted.next
        node_before_deleted.next = None
        return new_head


    



        