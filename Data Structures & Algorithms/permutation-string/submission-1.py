class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get lengths of both strings
        n, m = len(s1), len(s2)

        # If s1 is longer than s2, it can't be a permutation substring
        if n > m:
            return False

        # Initialize count arrays for both strings
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Count occurrences of characters in s1 and the first n characters of s2
        for i in range(n):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Check if the initial window is a permutation
        if s1_count == s2_count:
            return True

        # Slide the window through s2
        for i in range(n, m):
            # Add the count of the new character entering the window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove the count of the character leaving the window
            s2_count[ord(s2[i - n]) - ord('a')] -= 1

            # Check if the current window is a permutation
            if s1_count == s2_count:
                return True

        # If no permutation is found, return False
        return False

# Time complexity: O(n)
# Space complexity: O(1)