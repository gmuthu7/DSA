class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def fn(pos,subset,s):
            if pos == len(nums):
                result.append(subset[:])
                return
            for num in nums:
                if num in s:
                    continue
                subset[pos] = num
                s.add(num)
                fn(pos+1,subset,s)
                s.remove(num)
        fn(0,[0]*len(nums),set())
        return result
        