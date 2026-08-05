"""
# Two Stacks
Intuition:
Instead of searching the whole stack to find the minimum every time, we can keep a second stack that always stores the minimum value up to that point.
So whenever we push a new value, we compare it with the current minimum and store the smaller one on the minStack.
This guarantees that the top of minStack is always the minimum of the entire stack — allowing getMin() to work in constant time.
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# class MinStack:

#     def __init__(self):
#         self.stack = []
        
#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return min(self.stack)
        
