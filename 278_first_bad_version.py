# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 and isBadVersion(1):
            return 1

        start = 1
        end = n
        
        while start <= end:
            mid = (start + end)//2
            # print(mid ,start, end)

            if not (isBadVersion(mid)):
                start = mid +  1
                # print("next half")
                

            elif isBadVersion(mid):
                end = mid - 1
                # print("first half")
        
        # print("Outside ", start, end, mid)
        if (isBadVersion(start)):
            return start 

        return mid
        

            


        