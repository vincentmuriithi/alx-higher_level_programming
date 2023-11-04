#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(N, board, col, solutions):
    if col == N:
        sol = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    sol.append([i, j])
        solutions.append(sol)
        return True
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens(N, board, col + 1, solutions) or res
            board[i][col] = 0
    return res

def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens(N, board, 0, solutions)
    for sol in solutions:
        print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
