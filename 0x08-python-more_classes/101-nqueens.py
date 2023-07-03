#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 3 2023

@author: Ernest Okiya
"""


def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if the current position is under attack by any previously placed queens
        # Check the current row
        for i in range(col):
            if board[row][i] == 1:
                return False
        # Check the upper diagonal
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        # Check the lower diagonal
        i = row
        j = col
        while i < n and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1
        return True

    def solve_util(board, col):
        if col >= n:
            # All queens have been placed successfully
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve_util(board, col + 1):
                    return True
                # Backtrack if the current configuration doesn't lead to a solution
                board[i][col] = 0
        return False

    # Create an empty chessboard
    board = [[0] * n for _ in range(n)]

    if solve_util(board, 0):
        # Print the solution
        for row in board:
            print(' '.join(['Q' if cell == 1 else '.' for cell in row]))
    else:
        print(f"No solution found for {n} queens.")


# Test the program
n = 8  # Change this value to solve for different board sizes
solve_n_queens(n)
