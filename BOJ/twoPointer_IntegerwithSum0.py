# 백준 7453 합이 0인 네 정수
# https://www.acmicpc.net/problem/7453

import sys

n = int(sys.stdin.readline())
A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

answer = 0
AB = {}
for i in range(n):
    for j in range(n):
        # AB의 합
        temp = A[i] + B[j]
        if temp in AB:
            AB[temp] += 1
        else:
            AB[temp] = 1
for i in range(n):
    for j in range(n):
        # CD의 합
        temp = C[i] + D[j]
        if -temp in AB:
            answer += AB[-temp]

print(answer)