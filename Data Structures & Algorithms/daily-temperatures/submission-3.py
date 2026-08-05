class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l, r = 0, 1
        res = [0] * len(temperatures)
        while l < len(temperatures) - 1:
            if r >= len(temperatures):
                l += 1
                r = l + 1
                continue
                
            if temperatures[l] < temperatures[r]:
                res[l] = r - l
                l += 1
                r = l + 1
            else:
                r += 1
        
        return res
