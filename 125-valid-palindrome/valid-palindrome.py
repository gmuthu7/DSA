class Solution(object):
    def is_alpha_numeric(self,c):
        a = ord(c)
        if 65 <= a <= 90 or 48 <= a <= 57 or 97 <= a <= 122:
            return True
        return False
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0 
        j = len(s) - 1
        while i <= j:
            l = s[i]
            r = s[j]
            if not self.is_alpha_numeric(l):
                i+=1
                continue
            if not self.is_alpha_numeric(r):
                j-=1
                continue
            if lower(l) != lower(r):
                return False
            i+=1
            j-=1
        return True
            
        