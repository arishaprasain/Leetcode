class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end = len(nums) - 1

        start = 0

        while start <= end:
            mid = (start + end)//2


            if nums[mid] < target:
                start = mid + 1
                
            elif nums[mid] > target:
                end = mid - 1
                

            elif nums[mid] == target:
                return mid


        return -1


        