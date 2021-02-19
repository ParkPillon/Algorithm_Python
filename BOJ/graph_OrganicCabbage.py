# 백준 1012 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def findGroups(mmap, N, M, target):  # 값이 target인 그룹 위치 파악
    visited = [[False] * M for _ in range(N)]
    groups = []
    for x in range(N):
        for y in range(M):
            if visited[x][y]:
                continue
            visited[x][y] = True
            group = []
            if mmap[x][y] == target:
                queue = deque([(x, y)])
                while queue:
                    temp_x, temp_y = queue.popleft()
                    group.append((temp_x, temp_y))
                    for i in range(4):
                        nx = temp_x + dx[i]
                        ny = temp_y + dy[i]
                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue
                        if mmap[nx][ny] == target and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
            if group:  # 그룹이 형성될 경우
                groups.append(group)
    return groups


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    mmap = [[0] * M for a in range(N)]
    for b in range(K):
        col, row = map(int, sys.stdin.readline().split())
        mmap[row][col] = 1
    groups = findGroups(mmap, N, M, 1)
    print(len(groups))
