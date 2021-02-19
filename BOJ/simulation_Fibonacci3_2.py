# 백준 2749 피보나치 수 3
# https://www.acmicpc.net/problem/2749
# 행렬 곱셈 활용


import sys

n = int(sys.stdin.readline())
n = n % 1500000
ansMat = (1, 1, 1, 0)


def matPow(A: tuple, B: tuple):
    return (
        (A[0] * B[0] + A[1] * B[2]) % 1000000,
        (A[0] * B[1] + A[1] * B[3]) % 1000000,
        (A[2] * B[0] + A[3] * B[2]) % 1000000,
        (A[2] * B[1] + A[3] * B[3]) % 1000000,
    )


def fibo(x):
    if x == 0 or x == 1:
        return x
    else:
        ans = (1, 1, 1, 0)
        for _ in range(x - 1):
            ans = matPow(ans, ansMat)
        return ans[1]


print(fibo(n))