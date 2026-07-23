class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = []
        new = nums1 + nums2
        new.sort()
        new_len = len(new)
        if new_len % 2 == 0:
            half =  new_len//2
            result = (new[half-1] + new[half])/2
        else:
            half =  new_len//2
            result = new[half]
        return result