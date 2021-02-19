# 백준 9663 N-Queen
# https://www.acmicpc.net/problem/9663
# back tracking 백트래킹 알고리즘

import sys

N = int(sys.stdin.readline())

count = 0
# 퀸이 배치될때마다 대각선 경로로 공격 가능한 루트
# 같은 루트에 있는 위치는 각각 (0,0), (0,N-1)으로부터 같은 거리를 가짐
# (0,3), (1,2), (2,1), (3,0) 한 루트 내에 존재
# (0,3), (1,4), (2,5), (3,6), (4,7) 한 루트 내에 존재
left_path = [False] * (2 * N - 1)  # 공격 가능한 루트
right_path = [False] * (2 * N - 1)
vertical_path = [False] * N


def getPath(row, col):  # (0,0)으로부터의 거리, (0,N-1)으로부터의 거리
    return (row + col, row + N - 1 - col)


def dfs(row, col):
    global count
    if row == N - 1:  # 마지막 줄
        count += 1
        return
    for next_c in range(N):
        left, right = getPath(row + 1, next_c)
        if left_path[left] or right_path[right] or vertical_path[next_c]:
            continue
        left_path[left] = True
        right_path[right] = True
        vertical_path[next_c] = True
        dfs(row + 1, next_c)
        left_path[left] = False
        right_path[right] = False
        vertical_path[next_c] = False


for i in range(N):  # 첫줄에 모든지점에 대해 탐색 시작
    left, right = getPath(0, i)
    left_path[left] = True
    right_path[right] = True
    vertical_path[i] = True
    dfs(0, i)
    left_path[left] = False
    right_path[right] = False
    vertical_path[i] = False
print(count)