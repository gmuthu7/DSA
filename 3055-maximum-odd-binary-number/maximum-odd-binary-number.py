class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        queue = deque()
        first_one = False
        for c in s:
            if c == "1":
                if not first_one:
                    first_one = True
                    continue
                queue.appendleft("1")
            else:
                queue.append("0")
        queue.append("1")
        return "".join(queue)
        
        