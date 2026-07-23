class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest = 0
    
        for num in numSet:
            streak = 1
            while (num + 1) in numSet:
                streak +=1
                num += 1
            longest = max(streak, longest)
        return longest            
             