import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create list of (distance, point) tuples
        distances = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            distances.append((distance, point))
        
        # Get k smallest distances
        k_closest = heapq.nsmallest(k, distances)
        
        return [point for _, point in k_closest]