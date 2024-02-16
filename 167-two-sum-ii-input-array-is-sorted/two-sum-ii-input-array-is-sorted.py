class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            l = numbers[i]
            r = numbers[j]
            if l + r > target:
                j-=1
            elif l + r < target:
                i+=1
            else:
                return [i+1,j+1]
                

        