from solver import solve_sudoku
from generator import generate_sudoku
from utils import check_validity

def main():
    # Generate and solve a Sudoku puzzle
    puzzle = generate_sudoku()
    print("Generated Sudoku Puzzle:")
    for row in puzzle:
        print(row)
    solution = solve_sudoku(puzzle)
    print("\nSolved Sudoku Puzzle:")
    for row in solution:
        print(row)

    # Check the validity of the solved puzzle
    if check_validity(solution):
        print("\nSolution is valid.")
    else:
        print("\nSolution is invalid.")

if __name__ == "__main__":
    main()
