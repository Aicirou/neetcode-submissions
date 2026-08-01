"""
Intuition:
Instead of restarting at every index like brute force, we can keep one window that always has unique characters.
We expand the window by moving the right pointer.
If we ever see a repeated character, we shrink the window from the left until the duplicate is removed.
This way, the window always represents a valid substring, and we track its maximum size.
It's efficient because each character is added and removed at most once.
"""
class Sliding_Window_Set:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])            
            res = max(res, r - l + 1)
        
        return res

# Time Complexity: O(n)
# SPace Complexity: O(m), m = total number of unique characters in the string

"""
Intuition:
Instead of removing characters one by one when we see a repeat, we can "jump the left pointer" directly to the correct position.
We keep a map that stores the last index where each character appeared.
When a character repeats, the earliest valid starting point moves to "one position after" its previous occurrence.
This lets us adjust the window in one step and always keep it valid, making the approach fast and clean.
"""
class Sliding_Window_HashMap:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

# Time Complexity: O(n)
# SPace Complexity: O(m), m = total number of unique characters in the string


Solution = Sliding_Window_Set