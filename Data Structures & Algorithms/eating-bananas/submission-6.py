import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(speed: int) -> bool:
            """
            Checks if all piles can be finished within h hours at the given speed.

            Args:
                speed: The eating speed (bananas per hour).

            Returns:
                True if all piles can be finished within h hours, False otherwise.
            """
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / speed)
            return hours_needed <= h

        # Find the maximum pile size to set the upper bound for the search space
        max_pile_size = max(piles)

        # Initialize the search space for the eating speed (k)
        left, right = 1, max_pile_size

        # Initialize the minimum speed found so far
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
            
