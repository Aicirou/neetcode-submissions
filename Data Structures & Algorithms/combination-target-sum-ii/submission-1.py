class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, curset, remaining):
            if remaining == 0:
                result.append(curset.copy())
                return
            if remaining < 0 or i == len(candidates):
                return
            
            #include candidates[i]
            curset.append(candidates[i])
            backtrack(i+1, curset, remaining - candidates[i])
            curset.pop()

            #skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curset, remaining)
        
        result = []
        candidates.sort()
        backtrack(0, [], target)
        return result