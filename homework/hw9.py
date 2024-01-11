def is_safe(board, row, col, n):
    # 检查同一列是否有皇后
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_eight_queens(board, row, n):
    if row == n:
        # 打印解
        for i in range(n):
            line = ['Q' if j == board[i] else '.' for j in range(n)]
            print(' '.join(line))
        print("\n")
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_eight_queens(board, row + 1, n)

def eight_queens(n):
    board = [-1] * n
    solve_eight_queens(board, 0, n)

if __name__ == "__main__":
    n = 8
    eight_queens(n)
