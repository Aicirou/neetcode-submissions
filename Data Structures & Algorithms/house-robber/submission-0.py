class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1: max money we can rob up to house i-2
        # rob2: max money we can rob up to house i-1
        rob1, rob2 = 0, 0

        # Pattern: [rob1, rob2, n, n+1, ...]
        # For each house, we decide: rob it (n + rob1) or skip it (rob2)
        for n in nums:
            # Calculate max money if we consider current house n
            # Option 1: rob current house n + rob1 (skip adjacent house)
            # Option 2: skip current house, take rob2 (previous max)
            temp = max(n + rob1, rob2)
            
            # Shift the window forward:
            # rob1 becomes rob2 (what was i-1 is now i-2)
            rob1 = rob2
            
            # rob2 becomes temp (current max becomes previous max)
            rob2 = temp
        
        # rob2 holds the maximum money we can rob from all houses
        return rob2