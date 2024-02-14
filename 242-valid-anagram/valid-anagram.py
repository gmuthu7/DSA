class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) < len(s):
            w = s
            s = t
            t = w
        a = [0]*26
        distinct = 0
        for c in s:
            c = ord(c) - ord('a')
            a[c]+=1
            if a[c] == 1:
                distinct+=1
        for c in t:
            c = ord(c) - ord('a')
            a[c]-=1
            if a[c] < 0:
                return False
            elif a[c] == 0:
                distinct-=1
        if distinct == 0:
            return True
        

        