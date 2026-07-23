class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total) -> # of ways

        def backtrack(i, total):
            #base case
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i,total)]
            #memoization
            dp[(i, total)] = (backtrack(i+1, total + nums[i]) + backtrack(i+1, total-nums[i]))
            return dp[(i, total)]
        return backtrack(0, 0)