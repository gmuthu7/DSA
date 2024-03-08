class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        largest = 0
        num_elements = 0
        for num in nums:
            d[num]+= 1
            if d[num] > largest:
                num_elements = 1
                largest = d[num]
            elif d[num] == largest:
                num_elements += 1
            
        return num_elements*largest