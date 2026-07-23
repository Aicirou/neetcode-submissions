class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp_max = curMax * num
            tmp_min = curMin * num
            curMax = max(tmp_max, tmp_min, num)
            curMin = min(tmp_max, tmp_min, num)
            res = max(res, curMax)
        return res