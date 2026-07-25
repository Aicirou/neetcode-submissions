# ============================================================
# Solution 1: Sorting
# Time: O(m * nlogn)
# Space: O(m * n)
# Where, "m" is the number of strings and "n" is the length of the longest string.
# ============================================================

class Solution_Sorting:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


# ============================================================
# Solution 2: HashMap
# Time: O(m * n)
# Space: O(m) or O(m * n) if the output groups are counted.
# ============================================================

class Solution_HashMap:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())


Solution = Solution_HashMap