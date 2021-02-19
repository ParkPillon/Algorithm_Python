# 백준 2098 외판원 순회
# https://www.acmicpc.net/problem/2098
# 비트마스킹

import sys

INF = int(1e9)
N = int(sys.stdin.readline())
costs = []
for _ in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (1 << N) for _ in range(N)]  # 현재위치와 방문상태에 따른 최소비용


def dfs(now, memo):
    if dp[now][memo]:  # 이미 계산된 경우
        return dp[now][memo]
    if memo == (1 << N) - 1:  # 모두 방문한 경우 출발지로 돌아가는 비용 반환
        return costs[now][0] if costs[now][0] else INF

    min_cost = INF
    for i in range(1, N):  # i부터 시작해서 이동 가능한 경로에 대해 최소 비용 계산
        if (memo >> i) % 2 == 0 and costs[now][i]:
            temp = dfs(i, memo | 1 << i)
            min_cost = min(min_cost, temp + costs[now][i])
    dp[now][memo] = min_cost
    return min_cost


print(dfs(0, 1))
