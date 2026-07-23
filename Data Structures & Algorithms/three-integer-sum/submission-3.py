class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            #skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #use pointer
            l,r = i+1, n-1
            while(l<r):
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum == 0:
                    #found a valid sum
                    result.append([nums[i] , nums[l] , nums[r]])

                    l +=1
                    r -=1

                    #skip duplicates
                    while l<r and nums[l] == nums[l-1]:
                        l +=1
                    # while l<r and nums[r] == nums[r+1]:
                    #     r -=1
                elif threeSum <0:
                    l +=1
                else:
                    r -=1
        return result