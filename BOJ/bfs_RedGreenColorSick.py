# 백준 10026 적록색약
# https://www.acmicpc.net/problem/10026

import sys
from collections import deque

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

groups = []
groups_sick = []
visited = [[False] * N for _ in range(N)]
visited_sick = [[False] * N for _ in range(N)]

for row in range(N):
    for col in range(N):
        color = board[row][col]
        # 일반적인 경우
        if not visited[row][col]:
            visited[row][col] = True
            group = []
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                group.append((r, c))
                for i in range(4):
                    nr = r + dx[i]
                    nc = c + dy[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    if not visited[nr][nc] and board[nr][nc] == color:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            if group:
                groups.append(group)

        # 적록색약의 경우
        if not visited_sick[row][col]:
            visited_sick[row][col] = True
            group = []
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                group.append((r, c))
                for i in range(4):
                    nr = r + dx[i]
                    nc = c + dy[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    if not visited_sick[nr][nc] and (
                        (board[nr][nc] == "B") == (color == "B")  # 두 값이 파랑인지 아닌지만 체크
                    ):
                        visited_sick[nr][nc] = True
                        queue.append((nr, nc))
            if group:
                groups_sick.append(group)

print(len(groups), len(groups_sick))