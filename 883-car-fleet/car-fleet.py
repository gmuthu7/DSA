class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        [(10,1),(9,3),(8,2),(3,3),(0,1)]
        """
        ts = sorted(zip(position,speed),key= lambda x: x[0],reverse=True)
        fleets = 0
        prev = None
        for t in ts:
            if prev is None:
                fleets+=1
                prev = t
            else:
                time = (target - prev[0])/float(prev[1])
                if time*t[1] + t[0] < target:
                    fleets+=1
                    prev = t
        return fleets
        