class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the element that appears only once in an array where every
        other element appears twice.

        Bitwise XOR (^) Properties Used:
        1. Self-Cancellation: A ^ A = 0
           (Matching pairs XORed together cancel out to 0)
        2. Identity Element: 0 ^ B = B
           (XORing any number with 0 leaves it unchanged)
        3. Commutative & Associative: Order does not matter.
           (A ^ B ^ A = (A ^ A) ^ B = 0 ^ B = B)

        Time Complexity: O(n) - Single pass through the array.
        Space Complexity: O(1) - Constant extra memory.
        """
        res = 0
        for num in nums:
            res ^= num
        return res