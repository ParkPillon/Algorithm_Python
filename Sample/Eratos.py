# 에라토스테네스의 체
# 특정 범위 안의 모든 소수 찾기
# 다수 자연수에 대한 소수 여부
# O(NloglogN) 시간복잡도 빠르지만 메모리를 많이 사용

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


print(Eratos(1000))
