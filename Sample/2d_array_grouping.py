# 2차원 배열 (NxN)에서 뭉쳐있는 그룹 찾기

import sys
from collections import deque

N = int(sys.stdin.readline())
mmap = []
for _ in range(N):
    mmap.append(list(map(int, list(sys.stdin.readline().strip()))))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[False] * N for _ in range(N)]
groups = []

for x in range(N):
    for y in range(N):
        if visited[x][y]:
            continue
        visited[x][y] = True
        group = []
        if mmap[x][y] == 1:
            queue = deque([(x, y)])
            while queue:
                temp_x, temp_y = queue.popleft()
                group.append((temp_x, temp_y))
                for i in range(4):
                    nx = temp_x + dx[i]
                    ny = temp_y + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if mmap[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        if group:  # 그룹이 형성될 경우
            groups.append(group)
