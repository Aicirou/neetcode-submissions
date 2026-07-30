class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)

# Prefix & Suffix Arrays
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         if n == 0:
#             return 0

#         leftMax = [0] * n
#         rightMax = [0] * n

#         leftMax[0] = height[0]
#         for i in range(1, n):
#             leftMax[i] = max(leftMax[i - 1], height[i])

#         rightMax[n - 1] = height[n - 1]
#         for i in range(n - 2, -1, -1):
#             rightMax[i] = max(rightMax[i + 1], height[i])

#         res = 0
#         for i in range(n):
#             res += min(leftMax[i], rightMax[i]) - height[i]
#         return res

# Time Complexity: O(n)
# Space Complexity: O(n)