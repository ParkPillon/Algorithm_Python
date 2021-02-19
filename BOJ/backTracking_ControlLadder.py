# 백준 15684 사다리 조작
# https://www.acmicpc.net/problem/15684

import sys

N, M, H = map(int, sys.stdin.readline().split())
ladders = [[False for _ in range(N + 1)] for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ladders[a][b] = True


def checkDest(i, ladders):
    for row in range(1, H + 1):
        if ladders[row][i]:
            i += 1
        elif ladders[row][i - 1]:
            i -= 1
    return i


def dfs(count, target, last_r):
    if count == target:
        for i in range(1, N + 1):
            if checkDest(i, ladders) != i:
                return
        else:
            print(count)
            exit()
    for row in range(last_r, H + 1):
        for col in range(1, N):
            if ladders[row][col] or ladders[row][col - 1] or ladders[row][col + 1]:
                continue
            ladders[row][col] = True
            dfs(count + 1, target, row)
            ladders[row][col] = False


for target in range(4):
    dfs(0, target, 0)
else:
    print(-1)
