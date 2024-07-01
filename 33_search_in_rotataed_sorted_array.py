class Solution:

    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # Determine which half is properly sorted
            if nums[start] <= nums[mid]:
                # Left half is sorted
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1