# 이코테 기출문제 Q.05

import sys

N, M = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(N):
    for j in range(i + 1, N):
        if weight[i] != weight[j]:
            answer += 1

print(answer)