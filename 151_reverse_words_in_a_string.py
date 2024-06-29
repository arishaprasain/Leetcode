class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        if not s:
            return


        str_list = s.split()
        # str_list.remove)
        print(str_list)

        for i in range(len(str_list)):
            if str_list:
                stack.append(str_list.pop())
            else:
                return " ".join(stack)

        return " ".join(stack)
