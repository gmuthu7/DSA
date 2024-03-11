class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        def fn(candidates,i,subset,rem):
            if i == len(candidates):
                return
            rem_ = rem-candidates[i]
            if rem_ > 0:
                subset.append(candidates[i])
                fn(candidates,i,subset,rem_)
                subset.pop()
                fn(candidates,i+1,subset,rem)
            elif rem_ == 0:
                result.append(subset+[candidates[i]])
        fn(candidates,0,[],target)
        return result
            
        