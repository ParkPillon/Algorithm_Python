# 백준 7576 토마토
# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
stock = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def checkStock(stock):  # 창고의 토마토가 모두 익었으면 True
    return all([all(st) for st in stock])


def findTomato(stock):  # 익은 토마토의 위치
    answer = []
    for i in range(N):
        for j in range(M):
            if stock[i][j] == 1:
                answer.append((i, j))
    return answer


if checkStock(stock):
    print(0)
    exit()
visited = [[False] * M for _ in range(N)]
queue = deque([])
total_day = 0
for tomato_i, tomato_j in findTomato(stock):
    queue.append((tomato_i, tomato_j, 0))  # 0일차의 토마토
    visited[tomato_i][tomato_j] = True
while queue:
    x, y, days = queue.popleft()
    total_day = days
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not visited[nx][ny] and stock[nx][ny] == 0:
            stock[nx][ny] = 1
            queue.append((nx, ny, days + 1))
            visited[nx][ny] = True

if checkStock(stock):
    print(total_day)
else:
    print(-1)