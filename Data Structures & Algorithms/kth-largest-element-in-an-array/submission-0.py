import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Maintain a min heap of size k
        heap = []
        
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:  # If current number is larger than smallest in heap
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]  # Root of min heap is the kth largest