class Reverse_String:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(v for v in s.lower() if ('a' <= v <= 'z' or '0' <= v <= '9'))
        
        return new_s == new_s[::-1]

# Time Complexity: O(n)
# Space Complexity: O(n)


class Two_Pointer:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1

        return True   
               
# Time Complexity: O(n)
# Space Complexity: O(1)


Solution = Reverse_String