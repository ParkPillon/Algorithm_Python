# 백준 13460 구슬 탈출 2
# https://www.acmicpc.net/problem/13460
# '.' 빈칸 '#' 장애물/벽 '0' 구멍 'R' 빨간 구슬 'B' 파란 구슬

import sys

N, M = map(int, sys.stdin.readline().split())
board = [["#"] * (M + 2) for _ in range(N + 2)]
for i in range(N):
    row = list(sys.stdin.readline().strip())
    for j in range(M):
        board[1 + i][1 + j] = row[j]


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def moveBall(direction, current):  # direction:(0 동 1 북 2 서 3 남) current: 구슬의 현재위치
    x, y = current
    nx = x + dx[direction]
    ny = y + dy[direction]


def moveLeft(red, blue):
    pass
