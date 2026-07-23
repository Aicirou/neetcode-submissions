class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)
        
    def helper(self, i, nums):
        # Base case: if we've processed all elements
        if i == len(nums):
            return [[]]  # Return list containing empty permutation

        # Get all permutations of remaining elements
        perms = self.helper(i + 1, nums)
        result = []
        
        # Insert current element at every possible position
        for p in perms:
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                result.append(pCopy)
                
        return result