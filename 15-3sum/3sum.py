class Solution(object):
    def twoSum(self,i,j,nums,target):
        res = []
        last_l = None
        last_r = None
        while i < j:
            l = nums[i]
            r = nums[j]
            if last_r == r or l + r > target:
                j-=1
                last_r = r
            elif last_l == l or l+r < target:
                i+=1
                last_l = l
            else:
                last_l = l
                last_r = r
                res.append([l,r,-target])
                i+=1
                j-=1
        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-1,-1,-1):
            val = nums[i]
            if i + 1 < len(nums) and val == nums[i+1]:
                continue
            if val<0:
                break
            r = self.twoSum(0,i-1,nums,-val)
            res.extend(r)
        return res
