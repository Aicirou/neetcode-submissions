class Solution:
    def trap(self, height: List[int]) -> int:
        #two pointers
        l, r = 0, len(height) - 1
        #store max
        maxL = height[l]
        maxR = height[r]
       
        trapSum = 0

        while(l<r):
            if maxL < maxR:
                l +=1
                maxL = max(maxL, height[l])
                #calculate trap
                trapSum += maxL - height[l]
                maxL = max(maxL, height[l])
            else:
                r -=1
                maxR = max(maxR, height[r])
                #calculate trap
                trapSum += maxR - height[r]

                
        return trapSum


