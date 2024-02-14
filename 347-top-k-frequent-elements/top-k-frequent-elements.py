class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        lst = sorted(d.items(),key=lambda x: x[1],reverse=True)[:k]
        return [l[0] for l in lst]