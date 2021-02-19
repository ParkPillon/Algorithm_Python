# 이코테 기출문제 Q.04

import sys


def solution(N, coins):
    target = 1
    for c in coins:
        if c > target:
            return target
        target += c
    return target


N = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()


print(solution(N, coins))
