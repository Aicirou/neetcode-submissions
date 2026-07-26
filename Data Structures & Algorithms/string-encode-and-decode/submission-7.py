class Solution:
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