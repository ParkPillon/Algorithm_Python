# 백준 2098 외판원 순회2
# https://www.acmicpc.net/problem/2098
# 완전 탐색

import sys

N = int(sys.stdin.readline())
costs = []
for _ in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))

visited = [0] * N

min_cost = int(1e9)


def dfs(start, now, n_city, cost):  # 출발 도시, 현재도시, 몇번째 도시인지, 현재까지의 총비용
    global min_cost
    if n_city == N:  # 마지막 도시일 경우
        if costs[now][start]:  # 마지막 도시에서 출발 도시로 갈 수 있다면
            min_cost = min(min_cost, cost + costs[now][start])  # 최소값 갱신
        return
    visited[now] = 1
    for new in range(N):
        if not visited[new] and costs[now][new]:  # 방문하지 않았고 갈수있는 도시
            dfs(start, new, n_city + 1, cost + costs[now][new])
    visited[now] = 0


dfs(0, 0, 1, 0)

print(min_cost)