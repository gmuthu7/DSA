class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx,num in enumerate(nums):
            num2 = target - num
            if num2 in d:
                return [idx,d[num2]]
            d[num] = idx

            
        