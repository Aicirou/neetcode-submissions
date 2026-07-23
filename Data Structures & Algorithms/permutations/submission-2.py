class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time complexity O(N! * N), Space complexity O(N)
        
        def dfs(i=0):
            if i == n:
                res.append(path[:])  # Add a copy of current path
            else:
                for num in nums:
                    if num not in path:  # Check if number already used
                        path.append(num)     # Choose
                        dfs(i + 1)          # Explore
                        path.pop()          # Unchoose (backtrack)
        
        path = []           # Current permutation being built
        n = len(nums)       # Length of input array
        res = []           # Result list to store all permutations
        dfs()              # Start DFS from position 0
        return res