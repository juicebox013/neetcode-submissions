class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            #this is the middle row 
            row = (top + bot) // 2

            #if the target is bigger than the largest number in the middle row, we need to move the top pointer down to the row above it.
            if target > matrix[row][-1]:
                top = row + 1

            #if the target is smaller than the smallest number in the middle row, we need to move the bottom pointer up to the row before it.
            elif target < matrix[row][0]:
                bot = row - 1
            
            #otherwise, it is in the middle row and we break out of this loop
            else:
                break

        
        if not (top <= bot):
            return False
            
        #now we are doing binary search on this middle row 
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
