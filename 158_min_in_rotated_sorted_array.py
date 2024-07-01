class Solution:
    def findMin(self, nums: List[int]) -> int:
        end = len(nums) -1
        start = 0


        while start < end:
            mid = (start + end)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid    

        return nums[start]







        