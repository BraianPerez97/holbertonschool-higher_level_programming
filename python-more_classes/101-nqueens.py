#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column above the current row
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                sys.stdout.write('Q ')
            else:
                sys.stdout.write('. ')
        sys.stdout.write('\n')
    sys.stdout.write('\n')

def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens_util(board, 0, N)

def solve_nqueens_util(board, row, N):
    if row == N:
        print_solution(board, N)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N)
            board[row][col] = 0

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_nqueens(N)

if __name__ == "__main__":
    main()
