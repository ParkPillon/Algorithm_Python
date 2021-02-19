# 백준 17472 다리 만들기 2
# https://www.acmicpc.net/problem/17472

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
mmap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[False] * M for _ in range(N)]
islands = []
# 섬의 위치 파악
for x in range(N):
    for y in range(M):
        if visited[x][y]:
            continue
        visited[x][y] = True
        island = []
        if mmap[x][y] == 1:
            queue = deque([(x, y)])
            while queue:
                temp_x, temp_y = queue.popleft()
                island.append((temp_x, temp_y))
                for i in range(4):
                    nx = temp_x + dx[i]
                    ny = temp_y + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if mmap[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        if island:
            islands.append(island)
