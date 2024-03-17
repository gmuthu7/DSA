class Solution(object):
    def insert_at(self,intervals,val):
        left = 0
        right = len(intervals) - 1
        while left <= right:
            mid = (left+right)//2
            if val < intervals[mid][0]:
                right = mid -1
            else:
                left = mid + 1
        return right
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        1 3 5
        """
        pos1 = self.insert_at(intervals,newInterval[0])
        pos2 = self.insert_at(intervals,newInterval[1])
        interval = [-1,-1]
        if pos1 == -1:
            interval[0] = newInterval[0]
            pos1 = 0
        elif newInterval[0] <= intervals[pos1][1]:
            interval[0] = min(intervals[pos1][0],newInterval[0])
        else:
            pos1+=1
            interval[0] = newInterval[0]
        if pos2 == -1:
            interval[1] = newInterval[1]
        elif newInterval[1] <= intervals[pos2][1]:
            interval[1] = max(intervals[pos2][1],newInterval[1])
        else:
            interval[1] = newInterval[1]
        return intervals[:pos1] + [interval] + intervals[pos2+1:]


        