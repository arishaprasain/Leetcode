
class MinStack(object):

    def __init__(self):
        self.t = -1
        self.bottom = -1
        self.stack = []
        self.min_stack = []
        
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # if first empty stack
        if (self.t == -1 and  self.bottom == -1):
            self.t += 1
            # print("top: ", self.t)
        
            
        #adding in non empty stackk
        else :
            self.t += 1
            # print("top: ", self.t, "element : ")
            
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:      # Push min val to a separate stack O(1)
            self.min_stack.append(val)

        return

        

    def pop(self):
        """
        :rtype: None
        """
        #if empty
        if (self.t == -1):
            return
             
        else:
            self.t -= 1
            x = self.stack.pop()
            if (x == self.min_stack[-1] ):          # Remove if the top most element happens to be the minimum value
                self.min_stack.pop()    
            # print("Popped element :", x)
            
        return
            

    def top(self):
        """
        :rtype: int
        """
        # print("inside top func : ", self.data, self.t)
        if not self.stack:
            return None
        return self.stack[self.t]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            return
        else:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()