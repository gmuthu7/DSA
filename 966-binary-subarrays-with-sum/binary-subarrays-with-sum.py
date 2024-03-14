class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix = 0
        d = defaultdict(int)
        d[0] = 1
        cntr = 0
        for num in nums:
            prefix += num
            cntr += d[prefix - goal]
            d[prefix]+=1
        return cntr
            