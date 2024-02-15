class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [0]*len(nums)
        for idx,num in enumerate(nums):
            prefix[idx] = (prefix[idx-1] if idx - 1 >= 0 else 1) *num
        suffix = 1
        print(prefix)
        for idx,num in enumerate(reversed(nums)):
            pos = len(nums)-idx-1
            nums[pos] = (prefix[pos-1] if pos - 1 >= 0 else 1)*suffix
            suffix = suffix * num
        return nums
            

            
        