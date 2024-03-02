class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = 0
        res = []
        while right < len(nums):
            r = nums[right]
            if r < 0:
                left+=1
                right+=1
            else:
                if left == right:
                    left-=1
                l = nums[left]
                while left >= 0 and abs(l) <= r:
                    res.append(l**2)
                    left-=1 
                    l = nums[left]  
                res.append(r**2)
                right+=1
        if left == len(nums):
            left-=1
        while left >= 0:
            res.append(nums[left]**2)
            left-=1
        return res
                


        