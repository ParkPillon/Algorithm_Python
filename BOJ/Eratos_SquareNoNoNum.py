# 백준 1016 제곱ㄴㄴ수
# https://www.acmicpc.net/problem/1016

import sys
import math


def Eratos(x):
    answer = []
    array = [True] * (x + 1)
    for i in range(2, int(math.sqrt(x)) + 1):
        if array[i]:
            j = 2
            while i * j <= x:
                array[i * j] = False
                j += 1
    for i in range(2, x + 1):
        if array[i]:
            answer.append(i)
    return answer


_min, _max = map(int, sys.stdin.readline().split())

primeNums = Eratos(int(_max ** 0.5) + 1)
squareNums = []
for prime in primeNums:
    squareNums.append(prime ** 2)

isSquareNum = [True] * (_max - _min + 1)  # min부터 min+1000000
for num in squareNums:
    j = _min // num
    while num * j <= _max:
        if num * j >= _min:
            isSquareNum[num * j - _min] = False
        j += 1
print(isSquareNum.count(True))
