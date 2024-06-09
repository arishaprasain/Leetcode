class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # APPROACH 1 ==> sorting and comparing to keep count
        # size = len(nums)

        # #sorting
        # nums.sort()

        # #checking
        # i = 1
        # count = 1
        # lcount = 1

        # if size == 0:
        #     return 0

        # while (i <= size - 1):
        #     if(nums[i] == nums[i-1]):
        #         i += 1
        #         continue
        #     elif(nums[i] == nums[i-1] + 1 ):
        #         count += 1
        #     else:
        #         count = 1
        #     lcount = max(lcount, count)
        #     i += 1

        # print("count", count)
        # print("lcount", lcount)
        # print("sorted", nums)
        # return lcount

        #APPROACH -2 ==> USING HASH MAPS
        size = len(nums)
        if size == 0:
            return 0

        #creating hmap
        hmap = set(nums)

        #keeping track of count
        count = lcount = 1

        #if size!= 0
        for i in range(len(nums)):
            #making sure I count from the beginning
            if nums[i] - 1 not in hmap:
                count = 1
                consecutive = nums[i] + 1
                while consecutive in hmap:
                    consecutive += 1
                    count += 1
                lcount = max(lcount, count)
        print(lcount, count)
        return lcount
