class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)

        # Check row by row
        row_num = 0
        while row_num < size:
            seen = set()
            i = 0
            while i < size:
                cell = board[row_num][i]
                i += 1

                if cell == ".":
                    continue
                if cell in seen:
                    return False
                else:
                    seen.add(cell)

            row_num += 1

        # Check col by col
        col_num = 0
        while col_num < size:
            i = 0
            seen = set()

            while i < size:
                cell = board[i][col_num]
                i += 1
                if cell == ".":
                    continue
                elif cell in seen:
                    return False
                else:
                    seen.add(cell)
            col_num += 1

        for grid_num in range(9):
            # row_start = (grid_num * 3) % 9
            # col_start = grid_num // 3

            row_start = (grid_num // 3) * 3  # Fixed: Groups blocks vertically
            col_start = (grid_num % 3) * 3   # Fixed: Groups blocks horizontally

            seen = set()

            for i in range(3):
                for j in range(3):
                    cell = board[row_start + i][col_start + j]


                    if cell == ".":
                        continue
                    elif cell in seen:
                        return False
                    else:
                        seen.add(cell)


        return True

        