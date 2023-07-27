#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = 0
try:
    N = int(sys.argv[1])
except:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

def solveNQueens(n):
    solutions = []
    solve(n, [], solutions)
    printSolutions(solutions)

def solve(n, queens, solutions):
    row = len(queens)
    if row == n:
        solutions.append(queens)
        return

    for col in range(n):
        if isValid(queens, row, col):
            tmp = queens[:]
            tmp.append(col)
            solve(n, tmp, solutions)

def isValid(queens, row, col):
    for r, c in enumerate(queens):
        if (c == col or
            c - col == row - r or
            c - col == r - row):
            return False
    return True

def printSolutions(solutions):
    for solution in solutions:
        print(str(solution).replace(',', '').replace('[', '').replace(']', ''))

solveNQueens(N)
