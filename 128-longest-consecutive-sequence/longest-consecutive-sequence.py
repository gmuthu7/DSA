class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        longest = 0
        for num in nums:
            if num in d:
                continue
            if num - 1 in d and num + 1 in d:
                longest = max(longest,d[num+1] - d[num-1]+1)
                temp = d[num-1]
                d[d[num-1]]= d[num+1] 
                d[d[num+1]] = temp
                d[num] = 1
            elif num - 1 in d:
                d[num] = d[num-1]
                longest = max(longest,num - d[num] +1)
                d[d[num-1]] = num
            elif num + 1 in d:
                d[num] = d[num+1]
                longest = max(longest,d[num] - num +1)                
                d[d[num+1]] = num
            else:
                d[num] = num
                longest = max(longest,1)                
        return longest

        