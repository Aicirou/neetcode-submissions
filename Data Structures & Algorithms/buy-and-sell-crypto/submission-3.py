class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
        
            r += 1
        
        return maxP

# Time Complexity: O(n)
# Space Complexity: O(1)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')
#         max_profit = 0
#         for price in prices:
#             min_price = min(min_price, price)
#             max_profit = max(max_profit, price - min_price)
#         return max_profit
