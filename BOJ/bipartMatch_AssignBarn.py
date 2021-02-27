# 백준 2188 축사 배정
# https://www.acmicpc.net/problem/2188

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    num, *barns = map(int, input().split())
    for b in barns:
        graph[i].append(b)
barn = [0] * (M + 1)  # i번 축사와 연결된 소 번호


def dfs(cow):
    if visited[cow]:  # 이미 탐색한 경우
        return False
    visited[cow] = 1
    for b in graph[cow]:
        if barn[b] == 0 or dfs(barn[b]):  # 빈 축사이거나 축사와 연결되어있던 소를 다른 축사에 연결 가능한 경우
            barn[b] = cow
            return True
    return False


for i in range(1, N + 1):
    visited = [0] * (N + 1)
    dfs(i)

answer = 0
for i in range(1, M + 1):
    if barn[i]:  # 배정된 소가 있을 때
        answer += 1
print(answer)