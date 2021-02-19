# 백준 1987 알파벳
# https://www.acmicpc.net/problem/1987

import sys

R, C = map(int, sys.stdin.readline().split())
board = []
for _ in range(R):
    board.append(list(sys.stdin.readline().strip()))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [False] * 26
maxCount = 0


def dfs(r, c, count):
    global maxCount
    findNext = False
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        new = board[nr][nc]
        chrOrd = ord(new)
        if not visited[chrOrd - 65]:
            findNext = True
            visited[chrOrd - 65] = True
            dfs(nr, nc, count + 1)
            visited[chrOrd - 65] = False
    if not findNext:  # 더이상 이동 불가
        maxCount = max(maxCount, count)


visited[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)
print(maxCount)
