class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(temperatures) - 1,-1,-1):
            temp = temperatures[i]
            while stack and stack[-1][1] <= temp:
                stack.pop()
            if not stack:
                temperatures[i] = 0
            else:
                temperatures[i]  = stack[-1][0] - i
            stack.append((i,temp))
        return temperatures
        