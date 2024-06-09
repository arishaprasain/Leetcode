import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pos = k
        self.heap = nums
        heapq.heapify(self.heap)     #making a heap

        #popping smaller elements until we have top kth elements in the heap


        if len(self.heap) > k:
            while(len(self.heap) > k ):
                heapq.heappop(self.heap)  
            

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        # if (len(self.heap) < self.pos):
        #     # return None
        if (len(self.heap) > self.pos):
        # while(len(self.heap) != self.pos ):
            heapq.heappop(self.heap) 
        return self.heap[0]

       




# # Your KthLargest object will be instantiated and called as such:
# kthLargest = KthLargest(3, [4, 5, 8, 2])
# kthLargest.add(3);   
# kthLargest.add(5);   
# kthLargest.add(10);  
# kthLargest.add(9);   
# kthLargest.add(4);  