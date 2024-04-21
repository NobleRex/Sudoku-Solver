from random import sample

def generate_sudoku():
    """
    Generates a Sudoku puzzle.
    """
    grid = [[0 for _ in range(9)] for _ in range(9)]
    nums = sample(range(1, 10), 9)  # Shuffle numbers 1 to 9
    for i in range(9):
        grid[i][i] = nums[i]  # Place shuffled numbers on the diagonal
    return grid
