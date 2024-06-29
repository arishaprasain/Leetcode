class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = j = 0


        if not t and not s:
            return True

        if not t:
            return False

        if not s:
            return True

        found = ""
        while i < len(s) and j < len(t):

            if s[i] != t[j]:
                j += 1
                
            elif s[i] == t[j]:
                found += s[i]
                i += 1
                j += 1

        
        return found == s
