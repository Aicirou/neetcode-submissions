"""
# Monotonic Stack (a specialized stack data structure that keeps its elements in a sorted order—either strictly increasing or decreasing)
Intuition:
We want to know how long it takes until a warmer day for each temperature.
A stack helps because it keeps track of days that are still waiting for a warmer temperature.
As we scan forward, whenever we find a temperature higher than the one on top of the stack, it means we just discovered the “next warmer day” for that earlier day.
We pop it, compute the difference in days, and continue.
This way, each day is pushed and popped at most once, making the process efficient.
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # indices
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        
        return res