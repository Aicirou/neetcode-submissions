class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        
        # Track products from left-to-right AND right-to-left
        prefix = suffix = 0
        
        for i in range(n):
            # Left-to-right product (prefix)
            # If prefix is 0, reset to 1 (using "or" trick)
            prefix = nums[i] * (prefix or 1)
            
            # Right-to-left product (suffix)
            # Process from end of array backwards
            suffix = nums[n - 1 - i] * (suffix or 1)
            
            # Update result with max of both directions
            res = max(res, max(prefix, suffix))
            
        return res