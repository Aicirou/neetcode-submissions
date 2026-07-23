class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to use the two-pointer approach
        nums.sort()
        result = []
        n = len(nums)

        # Traverse the array
        for i in range(n):
            # Skip duplicates for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two-pointer technique for the remaining part of the array
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # while left < right and nums[right] == nums[right + 1]:
                    #     right -= 1

                elif current_sum < 0:
                    # Move left pointer to increase the sum
                    left += 1
                else:
                    # Move right pointer to decrease the sum
                    right -= 1

        return result
