class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {
            "*": lambda a,b : a*b,
            "/": lambda a,b: int(a/float(b)),
            "-": lambda a,b: a-b,
            "+": lambda a,b: a+b
        }
        for token in tokens:
            if token in ops:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(ops[token](op2,op1))
            else:
                stack.append(int(token))
        return stack.pop()