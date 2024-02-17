import heapq
class Solution(object):
        
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        heap = []
        for idx in range(1,len(heights)):
            diff = heights[idx] - heights[idx-1]
            if diff <= 0:
                continue
            if len(heap) < ladders:
                heapq.heappush(heap,diff)
                continue
            smallest = heapq.heappushpop(heap,diff)
            bricks -= smallest
            if bricks < 0:
                return idx -1         
            
        return len(heights) - 1


            

        