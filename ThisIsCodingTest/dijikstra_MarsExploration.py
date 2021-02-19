# 이코테 388 화성 탐사
# ACM-ICPC 기출

import sys
from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            cost = res[x][y] + mmap[nx][ny]
            if visited[nx][ny]:  # 이미 방문한 경우
                if res[nx][ny] > cost:
                    res[nx][ny] = cost
                    queue.append((nx, ny))
            else:
                res[nx][ny] = cost
                visited[nx][ny] = True
                queue.append((nx, ny))


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    mmap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    res = [[0] * N for _ in range(N)]
    res[0][0] = mmap[0][0]
    visited = [[False] * N for _ in range(N)]
    bfs(0, 0)
    print(res[N - 1][N - 1])
