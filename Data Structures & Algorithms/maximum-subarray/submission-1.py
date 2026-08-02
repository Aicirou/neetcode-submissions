class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        _max, _sum = nums[0], 0
        for num in nums:
            if _sum < 0:
                _sum = 0
            
            _sum += num
            _max = max(_max, _sum)
        return _max


