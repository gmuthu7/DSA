class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        min_end = points[0][1]
        arrows = 1
        for idx,point in enumerate(points,1):
            if point[0] <= min_end:
                min_end = min(min_end,point[1])
            else:
                arrows+=1
                min_end = point[1]
        return arrows 