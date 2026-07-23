class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        l, r = 0,len(heights) - 1

        while(l<r):
            mx_area = (r-l) * min(heights[l], heights[r])
            mx = max(mx, mx_area)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1

        return mx