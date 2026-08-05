import math
from typing import List
"""
Intuition:
Instead of checking every speed one by one, we notice that the total time needed decreases as the eating speed increases.
This means the answer lies in a sorted search space from 1 to max(piles).

Because the search space is ordered, we can use binary search to efficiently find the smallest speed that allows finishing the piles within h hours.
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(speed: int) -> bool:
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / speed)
            return hours_needed <= h

        # Upper bound for the search space
        max_pile_size = max(piles)

        # Initialize the search space for the eating speed (k)
        left, right = 1, max_pile_size
        min_speed = max_pile_size

        # Perform binary search to find the minimum speed
        while left <= right:
            mid = (left + right) // 2

            if can_finish(mid):
                min_speed = mid  # Update minimum speed
                right = mid - 1   # Try a smaller speed
            else:
                left = mid + 1    # Need a larger speed

        return min_speed
            
