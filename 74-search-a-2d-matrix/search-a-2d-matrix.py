class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix[0])* len(matrix) - 1
        row_size, col_size = len(matrix), len(matrix[0])
        while l <= h:
            mid = (h + l) // 2
            mid_row = mid // col_size 
            mid_col = mid - mid_row * col_size
            if matrix[mid_row][mid_col] < target:
                l = mid + 1
            elif matrix[mid_row][mid_col] > target:
                h = mid - 1
            else:
                return True
            
        return False

