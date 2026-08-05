"""
Intuition:
A stack fits Reverse Polish Notation perfectly because the most recent numbers are always the ones used next.
As we scan the tokens:

When we see a number, we push it onto the stack.
When we see an operator, we pop the top two numbers, apply the operation, and push the result back.
This way, the stack always holds the intermediate results, and the final remaining value is the answer.
It is clean, efficient, and directly follows how RPN is meant to be evaluated.
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                case _:
                    stack.append(int(t))   
        return stack[0]