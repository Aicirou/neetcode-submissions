# 1. Hash Map

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


# Time & Space Complexity
# Time complexity: O(n+m)
# Space complexity: O(1) since we have at most 26 different characters.


# 2. Hash Table (Using Array)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         count = [0] * 26
#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1
#             count[ord(t[i]) - ord('a')] -= 1

#         for val in count:
#             if val != 0:
#                 return False
#         return True


# 3. Sorting

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         return sorted(s) == sorted(t)

# Time & Space Complexity
# Time complexity: O(nlogn + mlogm)
# Space complexity: O(1) or O(n+m) depending on the sorting algorithm.
