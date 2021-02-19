# 백준 11051 이항 계수 2
# https://www.acmicpc.net/problem/11051

import sys

N, K = map(int, sys.stdin.readline().split())
a, b = 1, 1
for _ in range(K):
    a *= N
    b *= K
    N -= 1
    K -= 1
print((a // b) % 1000000007)
