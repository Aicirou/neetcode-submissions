import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)   # e.g., -8 (represents 8)
            second = heapq.heappop(stones)  # e.g., -7 (represents 7)
            
            if first != second:  # If stones have different weights
                heapq.heappush(stones, first - second)  # -8 - (-7) = -1 (represents 1)
        
        return abs(stones[0]) if stones else 0