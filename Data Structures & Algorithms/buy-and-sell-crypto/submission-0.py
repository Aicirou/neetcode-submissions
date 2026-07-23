class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max = 0
        l, r = 0, 1
        while(r < len(prices)):
            if prices[r]-prices[l] <= 0:
                l = r
            else:
                profit = prices[r]-prices[l]
                _max = max(_max, profit)
            r +=1
        return _max