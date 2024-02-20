class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        ADOBECODEBANC
        """
        d1 = {}
        d2 ={}
        res = None
        tot1 = tot2 = 0
        for c in t:
            d1[c] = d1.get(c,0)+1
            tot1+=1
        i = j = 0
        while j < len(s):
            c = s[j]
            if c in d1:
                d2[c] = d2.get(c,0) + 1
                if d2[c] <= d1[c]:
                    tot2+=1
            while tot2 == tot1:
                if not res or res[1] - res[0] + 1 > j - i + 1:
                    res = (i,j)
                b = s[i]
                if b in d1:
                    if d2[b] == d1[b]:
                        tot2-=1
                    d2[b]-=1
                i+=1
            j+=1
        return "" if not res else s[res[0]:res[1]+1]
                

        