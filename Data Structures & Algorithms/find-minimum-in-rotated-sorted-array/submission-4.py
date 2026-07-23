class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res_min = float('inf')

        while(l<=r):
            mid = (l+r) // 2

            if nums[mid] < res_min:
                res_min = nums[mid]
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l = mid + 1
        
        return res_min
            

        