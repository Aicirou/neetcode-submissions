class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(v for v in s.lower() if ('a' <= v <= 'z' or '0' <= v <= '9'))
        print(s)
        l, r = 0, len(s)-1
        while(l<=r):
            if s[l] != s[r]:
                return False
            l +=1
            r -=1
        return True