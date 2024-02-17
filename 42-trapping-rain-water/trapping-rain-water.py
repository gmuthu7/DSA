class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        stack = [(0,height[0])]
        res = 0
        for i in range(1,len(height)):
            h = height[i]
            while len(stack) > 0 and stack[-1][1] <= h:
                if len(stack) >= 2:
                    res+= (min(stack[-2][1],h) - stack[-1][1])* (i - stack[-2][0] - 1)
                stack.pop()
            stack.append((i,h))
        return res
        
        