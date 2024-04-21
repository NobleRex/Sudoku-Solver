def solve_sudoku(grid):
    """
    Solves a Sudoku puzzle using backtracking.
    """
    def is_valid(row, col, num):
        """
        Checks if it's valid to place 'num' in the given cell (row, col).
        """
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    def solve():
        """
        Recursive function to solve Sudoku using backtracking.
        """
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(i, j, num):
                            grid[i][j] = num
                            if solve():
                                return True
                            grid[i][j] = 0
                    return False
        return True

    if solve():
        return grid
    else:
        return None
