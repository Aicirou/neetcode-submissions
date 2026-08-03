from functools import cache
from math import inf
import sys
sys.setrecursionlimit(9999)

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """Returns the maximum score difference
        (current player score - opponent score)
        starting from index i.
        """
        n = len(stoneValue)

        @cache
        def dfs(i):
            if i >= n:
                # No stones left, so no score difference.
                return 0 
            
            best, take = -inf, 0

            # Try taking 1, 2, or 3 stones.
            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]

                # If we take stones worth 'take',
                # the opponent will then play optimally from j + 1.
                #
                # dfs(j + 1) represents the opponent's advantage
                # from the remaining game.
                #
                # Therefore our net advantage becomes:
                #   take - dfs(j + 1)
                best = max(best, take - dfs(j + 1))

            return best
        
        # Maximum score difference Alice can achieve
        # over Bob when the game starts.
        diff = dfs(0)
        
        # Positive difference => Alice wins.
        if diff > 0:
            return "Alice"

        # Negative difference => Bob wins.
        elif diff < 0:
            return "Bob"

        # Zero difference => Tie.
        return "Tie"