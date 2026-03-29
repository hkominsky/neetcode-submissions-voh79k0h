class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    row_key = (row, num)
                    col_key = (num, col)
                    grid_key = (row // 3, col // 3, num)

                    if row_key in seen or col_key in seen or grid_key in seen:
                        return False

                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(grid_key)

        return True