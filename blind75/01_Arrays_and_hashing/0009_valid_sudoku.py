# determine if a given sudoku board is valid

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_valid_row(board) and 
               self.is_valid_col(board) and
               self.is_valid_square(board))
    
    def is_valid_row(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid_values(row):
                return False
        return True
    
    def is_valid_col(self, board: List[List[str]]) -> bool:
        for col in zip(*board):
            if not self.is_valid_values(col):
                return False
        return True
    
    def is_valid_square(self, board: List[List[str]]) -> bool:
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not self.is_valid_values(square):
                    return False
        return True
    
    def is_valid_values(self, unit: List[str]) -> bool:
            unit = [i for i in unit if i != '.']
            return len(set(unit)) == len(unit)
