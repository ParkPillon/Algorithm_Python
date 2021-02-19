# 백준 14503 로봇 청소기
# https://www.acmicpc.net/problem/14503

import sys

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]
N, M = map(int, sys.stdin.readline().split())
R, C, D = map(int, sys.stdin.readline().split())
mmap = []
for _ in range(N):
    mmap.append(list(map(int, sys.stdin.readline().split())))

count = 0
visited = [[0] * M for _ in range(N)]

while True:
    # 1번 과정
    count += 1
    visited[R][C] = count
    # 2번 과정
    stop = False
    isSearching = True
    while isSearching:
        for _ in range(4):
            D = (D - 1) % 4  # 왼쪽 회전
            nr, nc = R + dx[D], C + dy[D]
            if mmap[nr][nc] == 0 and not visited[nr][nc]:
                R, C = nr, nc
                isSearching = False
                break
        else:  # 네 방향 모두 청소불가
            nr, nc = R - dx[D], C - dy[D]
            if mmap[nr][nc] == 1:  # 뒤쪽 방향이 벽
                stop = True
                break
            else:
                R, C = nr, nc
    if stop:
        break
print(count)