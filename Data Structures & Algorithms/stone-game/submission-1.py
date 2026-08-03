# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         return True

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
    
        seen = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l,r) in seen:
                return seen[(l,r)]

            l_sum = piles[l] - dfs(l + 1, r)
            r_sum = piles[r] - dfs(l, r - 1)
            
            res = max(l_sum, r_sum)

            seen[(l,r)] = res
            return res

        return dfs(0,0) > 0