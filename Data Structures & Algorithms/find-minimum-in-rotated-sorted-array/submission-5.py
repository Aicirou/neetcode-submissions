# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         l, r = 0, len(nums) - 1
#         _min = float("inf")

#         while l <= r:
#             mid = (l + r) // 2
            
#             if nums[mid] < _min:
#                 _min = nums[mid]
#                 if nums[r] < nums[mid]:
#                     l = mid + 1
#                 else: 
#                     r = mid - 1
#             else:
#                 l = mid + 1
        
#         return int(_min)

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        _min = float('inf')

        while l <= r:
            mid = (l + r) // 2

            # If the left half is sorted
            if nums[l] <= nums[mid]:
                _min = min(_min, nums[l])
                l = mid + 1
            else:
                _min = min(_min, nums[mid])  
                r = mid - 1

        return int(_min)
