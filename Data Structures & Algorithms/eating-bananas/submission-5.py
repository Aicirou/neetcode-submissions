import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_correct(mid):
            count_hours = 0
            for pile in piles:
                res = math.ceil(pile / mid)
                count_hours += res
            if count_hours > h:
                return 1
            elif count_hours <= h:
                return -1


        max_pile = float('-inf')
        for pile in piles:
            max_pile = max(max_pile, pile)

        l, r = 1, max_pile - 1

        min_k = max_pile

        while(l <= r):
            mid = (l+r) // 2
            if is_correct(mid) < 0:
                min_k = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return min_k
            
