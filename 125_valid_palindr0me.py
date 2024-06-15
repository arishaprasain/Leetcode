class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # delimeters = ".,!:-@#$%^&*_+=)(`[{}]/\' " ""
        # for delimeter in delimeters:
        #     # print(delimeter)
        #     s = s.replace(delimeter, ' ')

        # s = s.lower()
        # s = s.split()
        # s = ''.join(s)
        # #print(s)
        # k = s[-1::-1]
        # # print(k)

        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        #print(filtered_chars)
        
        
        return filtered_chars == filtered_chars[::-1]

       