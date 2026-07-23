"""
LeetCode 78: Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.

Time: O(2^n) - We generate 2^n subsets, each taking O(n) time to copy
Space: O(n) - Recursion depth is n, path array uses O(n) space
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []

        def backtrack(start: int, path: list[int]):
            # Add current subset to result (make a copy to avoid reference issues)
            res.append(path[:])

            # Try including each remaining element
            for i in range(start, len(nums)):
                # Include nums[i] in current subset
                path.append(nums[i])
                # Recursively generate subsets starting from next index
                backtrack(i + 1, path)
                # Backtrack: remove nums[i] to try next possibility
                path.pop()

        # Start backtracking with empty path
        backtrack(0, [])
        return res
