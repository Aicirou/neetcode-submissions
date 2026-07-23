class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumofSquares(n)
            if n == 1:
                return True
        return False
    
    def sumofSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10        # Get the last digit
            digit = digit ** 2    # Square it
            output += digit       # Add to sum
            n = n // 10          # Remove the last digit
        return output