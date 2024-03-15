class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        prefix = 1
        for idx,num in enumerate(nums):
            prefix *= num
            res[idx] = prefix
        postfix = 1
        for idx in range(len(nums)-1,-1,-1):
            num = nums[idx]
            res[idx] = (res[idx-1] if idx>=1 else 1) *postfix
            postfix *= num
        return res
            
        
            

            
        