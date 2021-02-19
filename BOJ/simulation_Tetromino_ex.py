# 백준 14500번 테트로미노 좋은 풀이
# https://www.acmicpc.net/problem/14500

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(x, y, cnt, result):
    global ans
    if result + max_val * (4 - cnt) < ans:
        return

    if cnt == 4:
        ans = max(ans, result)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            if cnt == 2:  # T자형 테트리스만들기
                dfs(x, y, cnt + 1, result + array[nx][ny])

            dfs(nx, ny, cnt + 1, result + array[nx][ny])
            visited[nx][ny] = False


n, m = list(map(int, input().split()))
array = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False for _ in range(m)] for _ in range(n)]
max_val = max(map(max, array))

ans = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, array[i][j])
        visited[i][j] = False

print(ans)