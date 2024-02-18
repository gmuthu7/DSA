class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = float("inf")
        profit = 0
        for price in prices:
            if m > price:
                m = price
            elif price - m > profit:
                profit = price - m
        return profit