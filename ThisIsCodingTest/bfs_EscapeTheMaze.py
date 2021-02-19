# 이코테 152p 미로 탈출
from collections import deque
import sys


def solution(N, M, maze):
    answer = 0
    return answer


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

distance = [[0] * M for n in range(N)]
queue = deque([(0, 0)])
distance[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
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
print(f"{maze[N-1][M-1]}칸입니다")
