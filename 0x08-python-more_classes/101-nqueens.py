import sys


def is_safe(board, row, col, N):
    # Check if the current position is safe for a queen

    # Check column on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(col):
        if col == N:
            solution = []
            for row in range(N):
                for col in range(N):
                    if board[row][col] == 'Q':
                        solution.append([row, col])
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'

    backtrack(0)

    return solutions


def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row, end=" ")
        print()


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
