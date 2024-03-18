class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        1,2,2,3,3,3,4
        1 2 3 4 12 13 14 23 24 123 134 234 124
        """
        nums.sort()
        res = []
        def fn(subset,i,last_insert_at):
            if i == len(nums):
                res.append(subset[:])
                return
            if last_insert_at == i-1 or i == 0 or nums[i] != nums[i-1]:
                subset.append(nums[i])
                fn(subset,i+1,i)
                subset.pop()
            fn(subset,i+1,last_insert_at)
        fn([],0,-1)
        return res



            


        
        