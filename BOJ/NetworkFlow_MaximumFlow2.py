# 백준 6086 최대 유량
# https://www.acmicpc.net/problem/6086
# Dinic's Algorithm
# # O(V^2E), bfs,dfs, 간선이 많은 경우 유용
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(52)]  # A~Z: 0~25 a~z :26~51
capa = [[0] * 52 for _ in range(52)]
flow = [[0] * 52 for _ in range(52)]
INF = float("inf")


def alphaToInt(ch):  # A~Z: 0~25 a~z :26~51
    if "A" <= ch <= "Z":
        return ord(ch) - ord("A")
    elif "a" <= ch <= "z":
        return ord(ch) - ord("a") + 26


for _ in range(N):
    a, b, c = input().split()
    a, b, c = alphaToInt(a), alphaToInt(b), int(c)
    adj[a].append(b)
    adj[b].append(a)
    capa[a][b] += c
    capa[b][a] += c


def leveling():
    # level 초기화
    for i in range(52):
        level[i] = -1
    level[0] = 0
    queue = deque()
    queue.append(0)
    while queue:
        now = queue.popleft()
        for new in adj[now]:
            if level[new] == -1 and (capa[now][new] - flow[now][new] > 0):
                level[new] = level[now] + 1
                queue.append(new)
    return level[25] != -1  #'Z'의 레벨이 책정이 되는가. 'Z'에 도달할 수 있는가


def dfs(cur, dest, f):
    if cur == dest:
        return f
    for new in adj[cur]:
        if level[new] == level[cur] + 1 and (capa[cur][new] - flow[cur][new] > 0):
            # 다음 레벨의 노드이며 간선 용량이 남은 경우
            # 다음 노드에서 다시 탐색
            df = dfs(new, dest, min(f, capa[cur][new] - flow[cur][new]))
            if df > 0:  # 경로가 형성되어 유량이 결정됨
                flow[cur][new] += df
                flow[new][cur] -= df
                return df
    return 0


level = [-1] * 52
total_flow = 0
while leveling():  #'Z'의 레벨이 책정됨 = 경로가 1개 이상
    while True:
        fl = dfs(0, 25, INF)
        if fl == 0:
            break
        total_flow += fl
print(total_flow)
