class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def fn(arr,i):
            if i == len(arr):
                return [[]]
            res = fn(arr,i+1)
            res2 = []
            for r in res:
                res2.append([arr[i]] + r)
            res.extend(res2)
            return res
        return fn(nums,0)
            
                
        