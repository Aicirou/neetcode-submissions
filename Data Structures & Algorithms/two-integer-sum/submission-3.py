from typing import List

# ============================================================
# Solution 1: Hash Map (One Pass)
# Time: O(n)
# Space: O(n)
# ============================================================

class Solution_1PassHashMap:
    def twoSum(self, nums, target):
        seen = {}  #val->index
        for i, v in enumerate(nums):
            diff = target - v
            if diff in seen:
                return [seen[diff], i]
            seen[v] = i
        return [] 


# ============================================================
# Solution 2: Sorting + Two Pointers
# Time: O(n log n)
# Space: O(n)
# ============================================================

class Solution_Sorting:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []  


# ============================================================
# Solution 3: Hash Map (Two Pass)
# Time: O(n)
# Space: O(n)
# ============================================================

class Solution_2PassHashMap:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []


# ============================================================
# Solution 3: Hash Map (Two Pass)
# Time: O(n^2)
# Space: O(1)
# ============================================================

class Solution_BruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


Solution = Solution_1PassHashMap