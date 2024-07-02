class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and  n != 0:
            print("cse 3")
            for i in range(n + m):
                nums1[i] = nums2[i]
            return

        if n == 0  and  m != 0:
            return

        i = j = 0
        for i in range(m + n ):
            if i < m and j < n and nums1[i] >= nums2[j] :
                temp = nums1[i]
                #swap
                nums1[i] = nums2[j]
                nums2[j] = temp
                nums2 = sorted(nums2)
                print("nums1 :", nums1, "/n nums2: ", nums2, i)
            elif  i >= m and nums1[i] == 0:
                print(nums1, nums2 , "------before---------")
                nums2 = sorted(nums2)
                nums1[i] = nums2[j]
                print(i, j , nums1[i], nums2[j])
                j += 1


"""BETTER SOLUTION
# Initialize three pointers
            # a.point at last number in nums1
            # b.point at the last number of nums2
            # c. point at the last index in nums1
        index1, index2, insertIndex = m - 1, n - 1, m + n - 1

        # While nums2 has numbers to merge
        while index2 >= 0:
            # Get the larger number and insert into the insertIndex of nums1
            if index1 >=0 and nums1[index1] > nums2[index2]:
                nums1[insertIndex] = nums1[index1]
                index1 -= 1
            else:
                nums1[insertIndex] = nums2[index2]
                index2 -= 1

            insertIndex -= 1






"""

            

            
        

        
        