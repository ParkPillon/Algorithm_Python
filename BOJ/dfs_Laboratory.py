# 백준 14502 연구소
# https://www.acmicpc.net/problem/14502
# 백트래킹 back Tracking
import sys

N, M = map(int, sys.stdin.readline().split())

map_lab = [list(map(int, sys.stdin.readline().split())) for n in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
new_map = [[0] * M for _ in range(N)]


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if new_map[nx][ny] == 0:
            new_map[nx][ny] = 2
            virus(nx, ny)


def count_safe():
    answer = 0
    for n in range(N):
        for m in range(M):
            if new_map[n][m] == 0:
                answer += 1
    return answer


def dfs(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                new_map[i][j] = map_lab[i][j]
        for i in range(N):
            for j in range(M):
                if new_map[i][j] == 2:
                    virus(i, j)
        max_safe = count_safe()
        result = max(result, max_safe)
        return
    for i in range(N):
        for j in range(M):
            if map_lab[i][j] == 0:
                map_lab[i][j] = 1
                count += 1
                dfs(count)
                map_lab[i][j] = 0
                count -= 1


dfs(0)
print(result)
