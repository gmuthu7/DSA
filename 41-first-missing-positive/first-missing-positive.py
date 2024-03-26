class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        3,4,-1,1 
        0,4,3,1
        1,0,3,4

        """
        for idx,num in enumerate(nums):
            initial_idx = idx
            while num != initial_idx + 1:
                if num <= 0 or num > len(nums) or num == idx+1:
                    num = 0
                    break
                idx = num-1
                num = nums[idx]
                nums[idx] = idx+1
            nums[initial_idx] = num
        idx = 0
        while idx < len(nums) and idx+1 == nums[idx]:
            idx+=1
        return idx+1
                
                
            
        