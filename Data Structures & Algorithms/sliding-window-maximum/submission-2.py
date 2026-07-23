from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Edge case: empty array or window size 0
        if not nums or k == 0:
            return []
        
        # Initialize deque and result list
        dq = deque()  # Stores indices
        res = []
        
        for right in range(len(nums)):
            # Remove indices from the back if the current element is greater
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            # Add the current index to the deque
            dq.append(right)
            
            # Calculate the left boundary of the current window
            left = right - k + 1
            
            # Remove the front index if it's outside the current window
            if dq[0] < left:
                dq.popleft()
            
            # Append the current max to the result list once the first window is complete
            if right >= k - 1:
                res.append(nums[dq[0]])
        
        return res
