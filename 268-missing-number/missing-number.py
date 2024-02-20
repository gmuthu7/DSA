class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        n = len(nums)
        for num in nums:
            s+=num
        if s == n*(n+1)/2:
            return 0
        else:
            return -s + n*(n+1)/2
        
        