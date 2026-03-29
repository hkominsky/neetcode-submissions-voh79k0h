class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row = 0 
        right_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1
        row = 0

        while left_row <= right_row:
            mid_row = (left_row + right_row) // 2
            if matrix[mid_row][-1] >= target and matrix[mid_row][0] <= target:
                row = mid_row
                break
            elif min(matrix[mid_row]) > target:
                right_row = mid_row - 1
            else:
                left_row = mid_row + 1

        while left_col <= right_col:
            mid_col = (left_col + right_col) // 2
            if matrix[row][mid_col] == target:
                return True
            elif matrix[row][mid_col] < target:
                left_col = mid_col + 1
            else:
                right_col = mid_col - 1

        return False