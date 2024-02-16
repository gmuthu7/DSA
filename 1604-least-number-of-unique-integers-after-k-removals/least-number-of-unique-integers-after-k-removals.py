class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        for a in arr:
            num = d.get(a,0)
            d[a] = num + 1
        c = sorted(d.items(),key=lambda x: x[1])
        s = 0
        for idx,val in enumerate(c):
            s+=val[1]
            if s>=k:
                if s == k:
                    return len(c) - idx -1
                else:
                    return len(c) - idx
        

        