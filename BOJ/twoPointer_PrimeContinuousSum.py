# 백준 1644 소수의 연속합
# https://www.acmicpc.net/problem/1644

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


N = int(sys.stdin.readline())
primeNums = Eratos(N)
end, count = 0, 0
temp_sum = 0
for start in range(len(primeNums)):
    while temp_sum < N and end < len(primeNums):
        temp_sum += primeNums[end]
        end += 1
    if temp_sum == N:
        count += 1
    temp_sum -= primeNums[start]

print(count)
