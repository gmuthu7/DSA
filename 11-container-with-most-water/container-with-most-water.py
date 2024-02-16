class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            left = height[l]
            right = height[r]
            area = max(area,(r-l)*min(left,right))
            if left <= right:
                l+=1
            elif left > right:
                r-=1
        return area
        