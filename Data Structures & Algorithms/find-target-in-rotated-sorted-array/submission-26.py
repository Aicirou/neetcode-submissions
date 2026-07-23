from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        Args:
            nums: A list of integers representing the rotated sorted array.
            target: The integer value to search for.

        Returns:
            The index of the target value if found, -1 otherwise.
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Determine which half of the array is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left sorted half
                else:
                    left = mid + 1   # Target is in the right unsorted half or not present
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in the right sorted half
                else:
                    right = mid - 1  # Target is in the left unsorted half or not present

        return -1  # Target not found