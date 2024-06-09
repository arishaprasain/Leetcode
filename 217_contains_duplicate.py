class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        occured = set()
        count = {}
        # making occured list
        for i in nums:
            if i not in occured:
                count[i] = 1
            else:
                count[i] += 1
                return True
            occured.add(i)

        #printing if any number appears at least twice in the dictionary
        # for value in count.values():
        #     print(value)
        #     if value >= 2:
        #         print(value)
        #         return True
