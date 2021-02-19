# 백준 1003 피보나치 함수
# https://www.acmicpc.net/problem/1003
import sys

T = int(sys.stdin.readline())

dp = [None] * 41
dp[0] = (1, 0)
dp[1] = (0, 1)


def fibo(x):
    global dp
    if dp[x]:
        return dp[x]
    answer = tuple([a + b for a, b in zip(fibo(x - 1), fibo(x - 2))])
    dp[x] = answer
    return answer


for _ in range(T):
    N = int(sys.stdin.readline())
    print(*fibo(N))
