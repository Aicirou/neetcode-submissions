class Solution:
    def isValid(self, s: str) -> bool:
        MAP = { "}": "{",")": "(","]": "[" }
        stack = []

        for ch in s:
            if ch in MAP:
                if stack and stack[-1] == MAP[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False