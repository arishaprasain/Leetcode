from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.counter = deque()  #to add time stamps and decide which request is older than 3k milliseconds
        
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.counter.append(t)
        while( self.counter and (t - 3000) > self.counter[0]):
            self.counter.popleft()
        return len(self.counter)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)