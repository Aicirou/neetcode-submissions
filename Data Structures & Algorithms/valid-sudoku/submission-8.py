class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):

                val = board[r][c]
                if val == ".":
                    continue  

                if (val in rows[r] 
                    or val in cols[c] 
                    or val in box[(r//3, c//3)]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                box[(r//3, c//3)].add(val)

        return True

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n ^ 2)
