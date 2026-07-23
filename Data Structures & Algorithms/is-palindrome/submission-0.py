class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        print(s)

        front = 0
        back = len(s) - 1

        while front <= back:
            if s[front] != s[back]:
                return False
            front += 1
            back -= 1
        return True