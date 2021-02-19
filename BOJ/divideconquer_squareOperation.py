# 백준 1629 곱셈
# https://www.acmicpc.net/problem/1629

import sys

a, b, c = map(int, sys.stdin.readline().split())


def square(a, b):
    if b == 0:
        return 1
    temp = ((square(a, b // 2)) ** 2) % c
    if b % 2 == 0:
        return temp
    else:
        return (temp * a) % c


print(square(a, b))