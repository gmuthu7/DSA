class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        m = val if not self.stack or self.min_stack[-1] >= val else self.min_stack[-1]
        self.stack.append(val)
        self.min_stack.append(m)
        

    def pop(self):
        """
        :rtype: None
        """
        self.min_stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()