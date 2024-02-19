class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        tot = 0
        for c1 in s1:
            d1[c1] = d1.get(c1,0) + 1
        i = 0
        j = 0
        while j < len(s2):
            end = s2[j]
            d2[end] = d2.get(end,0) + 1
            tot+=1
            while d2[end] > d1.get(end,0):
                start = s2[i]
                d2[start] -= 1
                tot-=1
                i+=1
            if tot == len(s1):
                return True
            j+=1
        return False
            


        