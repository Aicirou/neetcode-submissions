class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def isCorrect(mid, i):
            if matrix[i][mid] > target:
                return 1
            elif matrix[i][mid] < target:
                return -1
            else:
                return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            l, r = 0, cols - 1

            while(l<=r):
                mid = (l+r) //2

                if isCorrect(mid, i) > 0:
                    r = mid -1
                elif isCorrect(mid, i) < 0:
                    l = mid + 1
                else:
                    return True
                    
        return False

                
