# 백준 1978 소수 찾기
# https://www.acmicpc.net/problem/1978

import sys
import math

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))


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


primeList = Eratos(max(array))
count = 0
for a in array:
    if a in primeList:
        count += 1

print(count)
