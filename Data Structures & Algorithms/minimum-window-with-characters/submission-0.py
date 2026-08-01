"""
Intuition:
We want the smallest window in s that contains all characters of t (with the right counts).
Instead of checking all substrings, we use a sliding window:

Expand the window by moving the right pointer r and adding characters into a window map.
Once the window has all required characters (i.e., it "covers" t), we try to shrink it from the left with pointer l to make it as small as possible while still valid.
During this process, we keep track of the best (smallest) window seen so far.
This way, we only scan each character at most two times, making it efficient and still easy to follow.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1

        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(countT)
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                # update the result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Pop from left of our window
                window[s[l]]-= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""

# Time Complexity: O(n + m)
# Space Complexity: O(k)
# Where, n is the length of the string s, m is the length of the string t, and k is the total number of unique characters in s and t.
