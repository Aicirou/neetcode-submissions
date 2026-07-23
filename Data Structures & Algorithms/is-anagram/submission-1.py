class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base case - if not equal in length
        if len(s) != len(t):
            return False
        
        # Calculate the repetition of characters
        repeat = {}
        for ch in s:
            repeat[ch] = repeat.get(ch, 0) + 1

        for ch in t:
            if ch not in repeat:
                return False

            repeat[ch] -= 1
            if repeat[ch] < 0:
                return False
        
        return all(v == 0 for v in repeat.values())
