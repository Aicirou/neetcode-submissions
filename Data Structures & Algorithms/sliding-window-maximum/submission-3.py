
#Optimal Solution: Monotonic Deque (O(n))
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # Stores indices of elements in decreasing order
        l = r = 0    # Left and right pointers of the sliding window

        while r < len(nums):
            # Remove all smaller elements from the back of the deque.
            # They can never become the maximum while nums[r] is in the window.
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add current index to the deque.
            q.append(r)

            # Remove the front index if it is outside the current window.
            if l > q[0]:
                q.popleft()

            # Once the window reaches size k,
            # the front of the deque contains the maximum element.
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1  # Slide the window forward

            r += 1

        return output

"""
Time complexity: O(n)
Space complexity: O(n)
"""


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if k == 1:
#             return nums

#         l, r = 0, k
#         res = []

#         while r <= len(nums):
#             _max = float('-inf')

#             for i in range(l, r):
#                 _max = max(_max, nums[i])

#             res.append(_max)
#             l += 1
#             r += 1

#         return res