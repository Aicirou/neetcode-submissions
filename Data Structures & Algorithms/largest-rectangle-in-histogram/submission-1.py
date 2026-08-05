"""
Intuition:
For each bar, we want to know how far it can stretch left and right before bumping into a shorter bar.
That distance tells us the widest rectangle where this bar is the limiting height.
To efficiently find the nearest smaller bar on both sides, we use a monotonic stack that keeps indices of bars in increasing height order.
This lets us compute boundaries in linear time instead of checking outward for every bar.
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))

                start = index
            
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea