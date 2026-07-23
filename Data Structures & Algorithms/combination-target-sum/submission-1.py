"""
LeetCode 39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
You may use the same number from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Time: O(2^(t/m)) - where t is target and m is the minimum candidate value
Space: O(t/m) - Maximum depth of recursion tree
"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []

        def backtrack(remaining: int, start: int, path: list[int]):
            if remaining == 0:
                # Found a valid combination
                res.append(path[:])
                return
            elif remaining < 0:
                # Exceeded the sum, no need to continue
                return

            for i in range(start, len(candidates)):
                # Include candidates[i] in the current combination
                path.append(candidates[i])
                # Recur with updated remaining target; allow same element by passing i
                backtrack(remaining - candidates[i], i, path)
                # Backtrack: remove last added element to try next candidate
                path.pop()

        # Start backtracking with the full target and an empty path
        backtrack(target, 0, [])
        return res
