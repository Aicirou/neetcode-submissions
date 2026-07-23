class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get dimensions of the board
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            """
            Depth-First Search to find if word can be formed starting from position (r, c)
            r: current row position
            c: current column position  
            i: current index in the word we're trying to match
            """
            
            # Base case: if we've matched all characters in the word, we found it!
            if i == len(word):
                return True
            
            # Check boundary conditions and character match:
            # - Out of bounds (row or column)
            # - Current character doesn't match word[i]
            # - Cell is already visited (marked with '#')
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False
            
            # Mark current cell as visited by temporarily changing it to '#'
            # This prevents us from using the same cell twice in one path
            board[r][c] = '#'
            
            # Recursively search in all 4 directions (up, down, right, left)
            # If any direction returns True, we found the word
            res = (dfs(r + 1, c, i + 1) or  # Search down
                   dfs(r - 1, c, i + 1) or  # Search up
                   dfs(r, c + 1, i + 1) or  # Search right
                   dfs(r, c - 1, i + 1))    # Search left
            
            # BACKTRACK: Restore the original character
            # This is crucial so other paths can use this cell
            board[r][c] = word[i]
            
            return res
        
        # Try starting the search from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                # If we find the word starting from this position, return True
                if dfs(r, c, 0):
                    return True
        
        # If we've tried all starting positions and didn't find the word
        return False