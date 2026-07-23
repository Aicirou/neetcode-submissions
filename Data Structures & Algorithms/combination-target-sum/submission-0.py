class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current.copy())
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, remaining - nums[i])  # i, not i+1
                current.pop()
        
        result = []
        backtrack(0, [], target)
        return result