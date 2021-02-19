# 백준 11050 이항 계수 1
# https://www.acmicpc.net/problem/11050

import sys
from math import factorial

N, K = map(int, sys.stdin.readline().split())
print(factorial(N) // (factorial(K) * factorial(N - K)))
