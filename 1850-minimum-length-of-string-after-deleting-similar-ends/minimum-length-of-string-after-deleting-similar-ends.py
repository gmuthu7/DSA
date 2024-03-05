class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        aabcca
        """
        left = 0
        right = len(s) - 1

        while left <= right and s[left] == s[right]:
            if left == right:
                return 1
            elif right == left + 1:
                return 0
            while right -1 > left and s[right-1] == s[right]:
                right-=1
            while left + 1 < right and s[left+1] == s[left]:
                left+=1
            left+=1
            right-=1
        return right - left + 1 if left < right else 0

            
            

        
        