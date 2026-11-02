class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #collections.defaultdict is creating a dictionary where every new key automatically gets an empty
        #set as its value.
        # EX: rows = {
        #           0: {"5", "3", "7"},
        #           1: {"6", "1", "9", "5"},
        #           2: {"9", "8", "6"}
        #      }
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) #box_key = (i // 3, j // 3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])


        return True
