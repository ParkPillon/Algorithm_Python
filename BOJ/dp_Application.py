# 백준 7579 앱
# https://www.acmicpc.net/problem/7579
# 비활성화할 앱을 골라서 최소 M의 메모리를 확보하는 문제 (그 과정에서 발생하는 비용 최소화)
# 남길 앱을 골라서 최대 (현재메모리 - M) 남기는 문제로 생각 => 비용 대신 가중치로 생각 => 가중치의 합 최대화
# 최소가중치로 최소 M의 메모리를 남기는 문제로도 생각할 수 있음

import sys

N, M = map(int, sys.stdin.readline().split())
mem = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

TOTAL = sum(mem)  # 총 메모리
dp = [[0] * (N + 1) for _ in range(sum(cost) + 1)]
for weight in range(1, sum(cost) + 1):
    for i in range(1, N + 1):
        if cost[i - 1] <= weight:  # i번 앱 포함 가능
            # i번 앱 포함했을때와 안했을 때 중 메모리가 더 큰것(많이 남는 경우)
            dp[weight][i] = max(
                dp[weight - cost[i - 1]][i - 1] + mem[i - 1], dp[weight][i - 1]
            )
        else:
            dp[weight][i] = dp[weight][i - 1]
        if dp[weight][i] >= M:
            print(weight)
            exit()