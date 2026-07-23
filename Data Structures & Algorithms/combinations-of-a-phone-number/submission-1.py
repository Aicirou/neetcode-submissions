class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle edge case where input string is empty
        if not digits:
            return []

        # Initialize result list
        res = []
        
        # Mapping of digits to their corresponding characters
        digitToChar = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # Backtracking function to generate all combinations
        def backtrack(i, curStr):
            # Base case: if the length of the current string is equal to the length of the input digits
            if len(curStr) == len(digits):
                # Append a copy of the current string to the result list
                res.append(curStr)
                return
            
            # Iterate over each character corresponding to the current digit
            for c in digitToChar[digits[i]]:
                # Recursively call the backtrack function with the next digit and the current string plus the current character
                backtrack(i+1, curStr + c)

        # Start the backtracking process with the first digit and an empty string
        backtrack(0, "")
        return res