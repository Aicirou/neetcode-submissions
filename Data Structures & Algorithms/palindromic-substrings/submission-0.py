class Solution:
    def countSubstrings(self, s: str) -> int:
        arr = list(s)
        res = []

        # Generate all contiguous substrings
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                res.append(arr[i:j+1])
        
        count = 0
        for substring in res:
            if self.isPali(substring):
                count += 1
        return count

    def isPali(self, arr):
        l, r = 0, len(arr)-1

        while l < r:
            if arr[l] == arr[r]:
                l += 1
                r -= 1
            else:
                return False
        return True