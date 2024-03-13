class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = n*(n+1)/2
        sq = math.sqrt(s)
        if int(sq) == sq:
            return int(sq)
        return -1
        