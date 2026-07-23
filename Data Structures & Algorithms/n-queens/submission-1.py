class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Sets to track occupied columns and diagonals for quick checks
        col = set()      # Tracks columns where queens are placed
        posDiag = set()  # Tracks positive diagonals (r + c)
        negDiag = set()  # Tracks negative diagonals (r - c)
        
        res = []  # List to store all valid board configurations
        # Initialize an n x n board with '.' representing empty cells
        board = [["."] * n for i in range(n)]
        
        # Backtracking function to place queens row by row
        def backtrack(r):
            # Base case: If all rows are filled, add the current board to results
            if r == n:
                copy = ["".join(row) for row in board]  # Create a string representation of the board
                res.append(copy)  # Append to results
                return
            
            # Try placing a queen in each column of the current row
            for c in range(n):
                # Skip if column or either diagonal is already occupied
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # Place the queen and update tracking sets
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"  # Mark the position on the board
                
                # Recurse to the next row
                backtrack(r + 1)
                
                # Backtrack: Remove the queen and reset tracking sets
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."  # Reset the board position
        
        backtrack(0)  # Start backtracking from row 0
        return res    # Return all valid solutions
