# 백준 11401 이항 계수
# https://www.acmicpc.net/problem/11401
# 페르마 소정리 활용
# 모듈러 거듭제곱법

import sys

N, K = map(int, sys.stdin.readline().split())

MOD = 1000000007


def power(x, y):
    ans = 1
    while y > 0:
        if y % 2 == 1:
            ans = (ans * x) % MOD
        x = (x * x) % MOD
        y //= 2
    return ans


def fact(x):
    ans = 1
    for i in range(2, x + 1):
        ans = (ans * i) % MOD
    return ans


if K == N or K == 0:
    print(1)
else:
    a, b, c = fact(N), fact(K), fact(N - K)
    print((a * power(b, MOD - 2) * power(c, MOD - 2)) % MOD)
