class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hmap = {}
        lst = []
        for num in arr:
            hmap[num] = 0
        for num in arr:
            hmap[num] += 1
        # print(hmap, hmap.values())
        for count in hmap.values():
            if count not in lst: 
                lst.append(count)
            else:
                return False
        # print(lst)
        return True
    
        