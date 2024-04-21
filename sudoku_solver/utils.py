def check_validity(grid):
    """
    Checks the validity of a Sudoku grid.
    """
    def is_valid_row(row):
        """
        Checks if a row is valid.
        """
        return len(set(grid[row])) == 9 and all(cell in range(1, 10) for cell in grid[row])

    def is_valid_column(col):
        """
        Checks if a column is valid.
        """
        return len(set(grid[i][col] for i in range(9))) == 9

    def is_valid_square(row, col):
        """
        Checks if a 3x3 square is valid.
        """
        square = [grid[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]
        return len(set(square)) == 9

    for i in range(9):
        if not is_valid_row(i) or not is_valid_column(i):
            return False
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not is_valid_square(row, col):
                return False
    return True
