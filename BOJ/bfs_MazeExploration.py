# 백준 2187 미로 탐색
# https://www.acmicpc.net/problem/2178

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
distance = [[0] * M for n in range(N)]
queue = deque([(0, 0)])
distance[0][0] = 1
while queue:
    temp_x, temp_y = queue.popleft()
    for i in range(4):
        nx = temp_x + dx[i]
        ny = temp_y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if maze[nx][ny] == 0:
            continue
        if maze[nx][ny] == 1:
            queue.append((nx, ny))
            maze[nx][ny] = maze[temp_x][temp_y] + 1
print(maze[N - 1][M - 1])
