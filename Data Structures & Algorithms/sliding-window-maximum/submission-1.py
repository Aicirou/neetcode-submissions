class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        l,r = 0, k
        res= []

        while(r <=len(nums)):
            _max = 0
            for i in range(l,r):
                _max = max(_max, nums[i])

            res.append(_max)
            l += 1
            r += 1
        return res