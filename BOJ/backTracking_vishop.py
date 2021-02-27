# 백준 1799 비숍
# https://www.acmicpc.net/problem/1799
# 우하향 대각선과 좌하향 대각선을 0~(2N-1) 의 idx값으로 표현

import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 좌하향 대각선의 사용 여부 (x,y)는 (x+y)에 해당
rs_diag = [0] * (2 * N - 1)  # 우하향 대각선의 사용 여부 (x,y)는 (x-y+N-1)번 대각선에 해당

answer = 0


def dfs(ls_idx, selected):  # 좌하향 대각선을 기준으로 탐색
    global answer
    if ls_idx == 2 * N - 1:
        answer = max(answer, selected)
        return
    avail = False
    for x in range(N):
        y = ls_idx - x
        if y < 0 or y >= N:  # 보드를 벗어나는 경우
            continue
        if board[x][y] == 0:  # 비숍을 놓을 수 없는 경우
            continue
        if rs_diag[x - y + N - 1] == 1:  # 우하향 대각선상에 비숍 존재
            continue
        avail = True  # 이번 좌하향 대각선상에 놓을 수 있는 칸이 하나라도 존재함
        rs_diag[x - y + N - 1] = 1
        dfs(ls_idx + 1, selected + 1)
        rs_diag[x - y + N - 1] = 0
    if not avail:  # 이번 좌하향 대각선상에 놓을 칸이 없는 경우
        dfs(ls_idx + 1, selected)


dfs(0, 0)
print(answer)