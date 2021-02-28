# 백준 6086 최대 유량
# https://www.acmicpc.net/problem/6086
# Edmonds-Karp, 에드몬드 카프
# O(VE^2), bfs
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

total_flow = 0  # 네트워크 전체의 최대 유량
while True:
    # 매번 A에서 Z까지의 경로를 탐색하고 그 경로의 최대 유량을 더해줌
    # 경로가 없을 때까지 탐색
    prev = [-1] * 52  # 경로를 저장하기 위한 배열
    queue = deque()
    queue.append(0)
    while queue:
        now = queue.popleft()
        for new in adj[now]:
            if prev[new] != -1:  # 방문한 노드의 경우
                continue
            if capa[now][new] - flow[now][new] > 0:  # 현재 노드에서 다음 노드로 흐를 수 있을 때
                prev[new] = now
                queue.append(new)
                if new == 25:  #'Z'에 다다른 경우 = 경로 완성
                    break

    if prev[25] == -1:  # Z까지의 경로가 없음
        break
    f = INF
    cur = 25  # 'Z'부터 시작해서 경로를 역으로 탐색하며 이 경로의 최대유량을 구함
    while cur != 0:
        last = prev[cur]
        f = min(f, capa[last][cur] - flow[last][cur])
        cur = last

    # 이 경로의 최대 유량: f
    # 해당 경로의 간선들에 f만큼의 유량을 더해줌. 반대간선엔 -f
    cur = 25
    while cur != 0:
        last = prev[cur]
        flow[last][cur] += f
        flow[cur][last] -= f
        cur = last
    total_flow += f

print(total_flow)