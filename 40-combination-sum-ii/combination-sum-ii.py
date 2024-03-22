class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        1 2 3 5
        """
        candidates = sorted(candidates)
        res = []
        def helper(subset,i,subtarget,last_pos):
            if subtarget == 0:
                res.append(subset[:])
                return
            if i == len(candidates):
                return
            num = candidates[i]
            if num <= subtarget:
                if candidates[i-1] != num or (i == last_pos + 1):
                    subset.append(num)
                    helper(subset,i+1,subtarget-num,i)
                    subset.pop()
                helper(subset,i+1,subtarget,last_pos)
        helper([],0,target,-1)
        return res
            

            
        