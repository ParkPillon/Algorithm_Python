# 백준 1261 알고스팟
# https://www.acmicpc.net/problem/1261
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(list(sys.stdin.readline().rstrip()))
res = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        print(f"{(x,y)}에 대해 ........")
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            print(f"{(nx,ny)}으로의 간선")
            cost = res[x][y] + int(maze[nx][ny])  # (x,y)를 거쳐서 (nx,ny)까지의 거리
            if visited[nx][ny]:  # 이미 방문한 경우
                if res[nx][ny] > cost:  # 새로운 값이 더 작을 경우 갱신
                    res[nx][ny] = cost
                    print(f"방문했지만 갱신 {(x,y)} -> {(nx,ny)}")
                    queue.append((nx, ny))
            else:
                res[nx][ny] = cost
                visited[nx][ny] = True
                queue.append((nx, ny))
                print(f"첫 방문 {(x,y)} -> {(nx,ny)}, cost: {cost}")


bfs(0, 0)
print(res[N - 1][M - 1])
