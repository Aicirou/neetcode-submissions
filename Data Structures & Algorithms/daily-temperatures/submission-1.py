class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = []

        for i in range(len(t)):
            count = 1
            j = i + 1
            while j < len(t):
                if t[i] < t[j]:
                    break
                j +=1
                count +=1
            count = 0 if j == len(t) else count
            res.append(count)
        return res
            
                
