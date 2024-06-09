class MyQueue(object):

    def __init__(self):
        self.top = -1
        self.s1 = []  #==> final stack as queue
        self.s2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if (not self.s2 and not self.s1):
            #self.s2.append(x)
            self.s1.append(x)
        else:
            while (len(self.s1) != 0) :
                self.s2.append(self.s1.pop())   # ==> s1 is empty at this point
            self.s1.append(x)                   # ==> the inserted element is pushed towards the end of stack 1

            # now popping all the elements of stack 2 and pushing to stack1
            while (len(self.s2) != 0) :
                self.s1.append(self.s2.pop())   # ==> s1 is empty at this point
                

    def pop(self):
        """
        :rtype: int
        """
        if not self.s1:
            return 
        else:
            #print("Before popping" , self.s1)
            x = self.s1.pop()
            #print ("Popped element: ", x)
            #self.s2.remove(x)
            
            return x        

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if (len(self.s1) == 0):
            return True
        else:
            return False
                    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()