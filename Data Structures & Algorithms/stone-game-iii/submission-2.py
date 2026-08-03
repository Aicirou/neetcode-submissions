# from functools import cache
# from math import inf
# import sys
# sys.setrecursionlimit(9999)

# class Solution:
#     def stoneGameIII(self, stoneValue: List[int]) -> str:
#         """Returns the maximum score difference
#         (current player score - opponent score)
#         starting from index i.
#         """
#         n = len(stoneValue)

#         @cache
#         def dfs(i):
#             if i >= n:
#                 # No stones left, so no score difference.
#                 return 0 
            
#             best, take = -inf, 0

#             # Try taking 1, 2, or 3 stones.
#             for j in range(i, min(i + 3, n)):
#                 take += stoneValue[j]

#                 # If we take stones worth 'take',
#                 # the opponent will then play optimally from j + 1.
#                 #
#                 # dfs(j + 1) represents the opponent's advantage
#                 # from the remaining game.
#                 #
#                 # Therefore our net advantage becomes:
#                 #   take - dfs(j + 1)
#                 best = max(best, take - dfs(j + 1))

#             return best
        
#         # Maximum score difference Alice can achieve
#         # over Bob when the game starts.
#         diff = dfs(0)
        
#         # Positive difference => Alice wins.
#         if diff > 0:
#             return "Alice"

#         # Negative difference => Bob wins.
#         elif diff < 0:
#             return "Bob"

#         # Zero difference => Tie.
#         return "Tie"

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Time complexity O(n), space complexity O(1)
        n = len(stoneValue)

        suffix1 = suffix2 = suffix3 = 0
        dp1 = dp2 = dp3 = 0

        for i in range(n - 1, -1, -1):
            res = stoneValue[i] + (suffix1 - dp1)
            if i + 2 <= n:
                n2 = stoneValue[i] + stoneValue[i + 1] + (suffix2 - dp2)
                res = max(res, n2)
            if i + 3 <= n:
                n3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + (suffix3 - dp3)
                res = max(res, n3)
            dp3 = dp2
            dp2 = dp1
            dp1 = res
            suffix3 = suffix2
            suffix2 = suffix1
            suffix1 += stoneValue[i]

        if dp1 > suffix1 - dp1:
            return "Alice"
        if dp1 == suffix1 - dp1:
            return "Tie"
        return "Bob"

        # stoneValue = [1,2,1,5]
        # n = 4
        # suffix1 = 9, suffix2 = 5, suffix3 = 6
        # dp1 = 4, dp2 = 8, dp3 = 6
        # i = 0
        # res = 4
        # n2 = 3
        # n3 = 4