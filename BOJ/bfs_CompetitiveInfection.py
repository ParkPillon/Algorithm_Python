# 백준 18405 경쟁적 전염
# https://www.acmicpc.net/problem/18405

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
testTube = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

S, X, Y = map(int, sys.stdin.readline().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def infect(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if testTube[nx][ny] == 0:
            testTube[nx][ny] = testTube[x][y]
            new_queue.append((nx, ny))


def setInitialVirus():
    res = []
    for virusType in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                if testTube[i][j] == virusType:
                    res.append((i, j))
    return res


queue = deque(setInitialVirus())
new_queue = deque([])
count = 0
while count < S:
    count += 1
    if not queue:
        break
    while queue:
        temp = queue.popleft()
        infect(*temp)
    queue = new_queue
    new_queue = deque([])

print(testTube[X - 1][Y - 1])
