# 백준 1799 비숍
# https://www.acmicpc.net/problem/1799
# 이분 매칭
# 좌하향 대각선, 우하향 대각선 두개의 그룹으로 나누고 이분 매칭

import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

DIAG = 2 * N - 1  # 대각선 수
graph = [[] for _ in range(DIAG)]  # i번 대각선에서 연결 가능한 우하향 대각선 번호
for i in range(DIAG):  # 좌하향 대각선을 기준으로 놓을수 있는 칸을 탐색
    for x in range(N):
        y = i - x
        if y < 0 or y >= N:
            continue
        if board[x][y] == 0:
            continue
        graph[i].append(x - y + N - 1)


linked = [-1] * DIAG  # 우하향 대각선 i와 연결된 좌하향 대각선 번호


def dfs(now):
    if visited[now]:
        return False
    visited[now] = 1
    for rdown in graph[now]:  # 현재 대각선에서 연결 가능한 대각선에 대해
        if linked[rdown] == -1 or dfs(linked[rdown]):  # 비어있거나 새로운 탐색이 가능할 경우
            linked[rdown] = now
            return True
    return False


for i in range(DIAG):
    visited = [0] * DIAG
    dfs(i)
answer = 0
for i in range(DIAG):
    if linked[i] != -1:
        answer += 1
print(answer)