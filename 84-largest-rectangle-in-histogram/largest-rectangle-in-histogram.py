class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        1,3,5,7,2
        """
        stack = []
        largest = 0
        for i in range(len(heights)):
            cntr = 0
            while stack and stack[-1][0] > heights[i]:
                cntr+=stack[-1][1]
                if largest < stack[-1][0] * cntr:
                    largest = stack[-1][0] * cntr
                stack.pop()
            stack.append((heights[i],cntr+1))
        cntr = 0
        while stack:
            cntr+=stack[-1][1]
            if largest < stack[-1][0] * cntr:
                largest = stack[-1][0] * cntr
            stack.pop()

        return largest


        