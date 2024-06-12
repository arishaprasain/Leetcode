class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList(object):
    
    def __init__(self):
        """
        
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index):
        """
        
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.val
    
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def addAtTail(self, val):
        """

        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def addAtIndex(self, index, val):

        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        new_node = ListNode(val)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        
        self.size += 1
    
    def deleteAtIndex(self, index):
        """
       
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            
            current.prev.next = current.next
            current.next.prev = current.prev
        
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
