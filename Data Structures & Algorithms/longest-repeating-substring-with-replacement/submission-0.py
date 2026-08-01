"""
Intuition:
We try to make a valid window where all characters become the same, but instead of checking every substring, we fix a target character c and ask:

"How long can the window be if we want the entire window to become c using at most k replacements?"

We slide a window across the string and count how many characters inside it already match c.
If the number of characters that don't match c is more than k, the window is invalid, so we shrink it from the left.
By doing this for every possible character, we find the longest valid window.

This idea is simple and beginner-friendly because we only track:

how many characters match c
how many replacements are needed
"""
class Sliding_Window_Set:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res

# Time Complexity: O(m * n)
# Space Complexity: O(m)
# Where, n is the length of the string and m is the total number of unique characters in the string.


"""
Intuition
We want the longest window where we can make all characters the same using at most k replacements.
The key insight is that the window is valid as long as:

window size – count of the most frequent character ≤ k

Why?
Because the characters that aren't the most frequent are the ones we would need to replace.

So while expanding the window, we track:

the frequency of each character,
the highest frequency we have seen in the window as it grows (maxf).
After we shrink from the left, maxf may be stale because we do not decrease it.
That can temporarily make the current window look valid even when its true current maximum frequency is smaller.
This is still correct because such a stale value never increases the answer beyond a window length that was already achievable when maxf was accurate.

If the window is too large under this tracked maxf, we shrink it from the left.
This gives us one clean sliding window pass.
"""
class Sliding_Window_HashMap:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

# Time Complexity: O(n)
# Space Complexity: O(m)
# Where, n is the length of the string and m is the total number of unique characters in the string.

Solution = Sliding_Window_HashMap