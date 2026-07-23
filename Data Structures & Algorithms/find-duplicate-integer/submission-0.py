class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nondupli = set()
        for val in nums:
            if val in nondupli:
                return val
            else:
                nondupli.add(val)
        return -1  # Return -1 if no duplicate is found (though problem states there will always be one)