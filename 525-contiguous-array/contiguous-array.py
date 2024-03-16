class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1010
        00110011
        0100011
        """
        count = 0
        longest = 0
        d = {}
        d[0] = -1
        for idx,num in enumerate(nums):
            if num == 0:
                count+=-1
            else:
                count+=1
            if count in d:
                if longest < idx-d[count]:
                    longest = idx-d[count]
            else:
                d[count] = idx
        return longest





        