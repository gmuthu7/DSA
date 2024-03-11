class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        res = ""
        for c in order:
            for _ in range(d[c]):
                d[c]-=1
                res+=c
            del d[c]
        for c in d:
            for _ in range(d[c]):
                d[c]-=1
                res+=c
        return res
        