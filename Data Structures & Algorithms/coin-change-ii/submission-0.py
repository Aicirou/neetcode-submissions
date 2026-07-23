class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: 1 way to make 0
    
        # IMPORTANT: Coins must be outer loop! (as idx moves forward)
        for coin in coins: 
            for amt in range(coin, amount + 1):
            # Recursion: take = helper(amt - coin, same_idx)
            # Bottom-up: dp[amt] += dp[amt - coin]
                dp[amt] += dp[amt - coin]
        return dp[amount]
