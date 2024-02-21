class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        -1 3 1 2 -1 1 2 5
        x+k=l
        """
        queue = deque()
        res = []
        idx = 0
        while idx < k-1:
            num = nums[idx]
            while queue and num > queue[-1][1]:
                queue.pop()
            queue.append((idx,num))
            idx+=1
        idx = 0
        while idx < len(nums) - k + 1:
            el = nums[idx+k-1]
            if queue and idx > queue[0][0]:
                queue.popleft()
            while queue and el > queue[-1][1]:
                queue.pop()
            queue.append((idx+k-1,el))
            res.append(queue[0][1])
            idx+=1

        return res
            


        
        
        