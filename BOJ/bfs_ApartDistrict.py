# 백준 2667 단지번호 붙이기
# https://www.acmicpc.net/problem/2667

import sys
from collections import deque

N = int(sys.stdin.readline())
mmap = []
for _ in range(N):
    mmap.append(list(map(int, list(sys.stdin.readline().strip()))))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[False] * N for _ in range(N)]
apartments = []
# 아파트 위치 파악
for x in range(N):
    for y in range(N):
        if visited[x][y]:
            continue
        visited[x][y] = True
        district = []  # 단지 정보
        if mmap[x][y] == 1:
            queue = deque([(x, y)])
            while queue:
                temp_x, temp_y = queue.popleft()
                district.append((temp_x, temp_y))
                for i in range(4):
                    nx = temp_x + dx[i]
                    ny = temp_y + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if mmap[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        if district:  # 단지가 형성될 경우
            apartments.append(district)
apartments.sort(key=lambda ap: len(ap))
print(len(apartments))
for ap in apartments:
    print(len(ap))