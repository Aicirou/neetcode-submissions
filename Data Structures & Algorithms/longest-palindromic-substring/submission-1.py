class Solution:
    def longestPalindrome(self, s: str) -> str:
        arr = list(s)
        res = []

        # Generate all substrings (contiguous sequences)
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                res.append(arr[i:j+1])
        
        maxArr = []
        for substring in res:
            if self.isPali(substring):
                maxArr = substring if len(substring) >= len(maxArr) else maxArr
        return "".join(c for c in maxArr)

    def isPali(self, arr):
        l, r = 0, len(arr)-1

        while l < r:
            if arr[l] == arr[r]:
                l += 1
                r -= 1
            else:
                return False
        return True