class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+','-','*','/'}

        for token in tokens:
            if token in operations:
                # remove last two
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a+b)
                if token == '-':
                    stack.append(a-b)
                if token == '*':
                    stack.append(a*b)
                if token == '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]

        
