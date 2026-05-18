class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        size = rows * cols

        low = 0
        hi = size - 1

        while low <= hi:
            middle = low + ((hi - low) // 2)

            row_idx = middle // cols
            col_idx = middle % cols

            res = matrix[row_idx][col_idx]

            if res == target:
                return True
            elif res < target:
                low = middle + 1
            else:
                hi = middle - 1

        return False