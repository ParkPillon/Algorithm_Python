# 백준 2239 스도쿠
# https://www.acmicpc.net/problem/2239

import sys

nums_row = [[False for _ in range(9)] for _ in range(9)]
nums_col = [[False for _ in range(9)] for _ in range(9)]
nums_box = [[False for _ in range(9)] for _ in range(9)]
board = []
blanks = []
for i in range(9):
    array = list(map(int, sys.stdin.readline().split()))
    board.append(array)
    for j in range(9):
        value = array[j]
        if value:  # 0이 아니면
            nums_row[i][value - 1] = True
            nums_col[j][value - 1] = True
            nth_box = i - i % 3 + j // 3
            nums_box[nth_box][value - 1] = True
        else:
            blanks.append((i, j))


def getCandidates(row, col):
    result = []
    for i in range(1, 10):
        nth_box = row - row % 3 + col // 3
        if nums_row[row][i - 1] or nums_col[col][i - 1] or nums_box[nth_box][i - 1]:
            continue
        result.append(i)
    return result


def dfs(count):
    if count == len(blanks):
        for b in board:
            print(*b)
        exit()
    row, col = blanks[count]
    for value in getCandidates(row, col):
        board[row][col] = value
        nums_row[row][value - 1] = True
        nums_col[col][value - 1] = True
        nth_box = row - row % 3 + col // 3
        nums_box[nth_box][value - 1] = True
        dfs(count + 1)
        # 탐색 후 원위치
        nums_row[row][value - 1] = False
        nums_col[col][value - 1] = False
        nums_box[nth_box][value - 1] = False


dfs(0)