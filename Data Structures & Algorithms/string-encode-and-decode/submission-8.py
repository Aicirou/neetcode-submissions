class Solution_DELIMITER :
    DELIM = "$#0@9#$"
    EMPTY = "$#EMPTY_LIST#$"

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return self.EMPTY
        return self.DELIM.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.EMPTY:
            return []
        return s.split(self.DELIM)

# Optimal

class Solution_Optimal:
    
    def encode(self, strs: List[str]) -> str:
        res = [] # -> 4#love
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j

        return res


Solution = Solution_Optimal