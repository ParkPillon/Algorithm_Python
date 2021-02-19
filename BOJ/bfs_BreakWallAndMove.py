# 백준 2206 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
# 0으로만 이동하지만 중간에 1개의 1은 포함 가능
# 방문 체크 배열을 3차원 배열로
# bfs의 새로운 테크닉
# 중요
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
mmap = []
for _ in range(N):
    mmap.append(list(map(int, list(sys.stdin.readline().strip()))))
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

visited = [[[0, 0] for __ in range(M)] for _ in range(N)]  # 벽을 뚫지않은 경우와 뚫은 경우
queue = deque([(0, 0, False)])  # (행, 열, 경로에 벽을 포함했는가)
visited[0][0][False] = 1
while queue:
    row, col, hasBreak = queue.popleft()
    count = visited[row][col][hasBreak]  # 현재 지점까지의 거리
    if row == N - 1 and col == M - 1:
        print(count)
        break
    for i in range(4):
        nr = row + dx[i]
        nc = col + dy[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if mmap[nr][nc] == 0 and not visited[nr][nc][hasBreak]:
            visited[nr][nc][hasBreak] = count + 1
            queue.append((nr, nc, hasBreak))
        elif (
            mmap[nr][nc] == 1 and not hasBreak and not visited[nr][nc][True]
        ):  # 이번에 벽을 부수는 경우
            visited[nr][nc][True] = count + 1
            queue.append((nr, nc, True))

else:
    print(-1)