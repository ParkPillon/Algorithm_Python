# 백준 1022 소용돌이 예쁘게 출력하기
# https://www.acmicpc.net/problem/1022

import sys


def getValue(r, c):
    if r == 0 and c == 0:
        return 1

    nth_cycle = max(abs(r), abs(c))
    start_value = (nth_cycle * 2 - 1) ** 2 + 1
    ith_num = 0
    if r == -nth_cycle:  # n번째 원에서 상단
        ith_num = (2 * nth_cycle) - 1 + (nth_cycle - c)
    elif r == nth_cycle:  # 하단
        ith_num = 3 * (2 * nth_cycle) - 1 + (nth_cycle + c)
    else:
        if c == nth_cycle:
            ith_num = (nth_cycle - 1) - r
        elif c == -nth_cycle:
            ith_num = 2 * (2 * nth_cycle) - 1 + (nth_cycle + r)
    return start_value + ith_num


r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
maxLen = 0
array = []
for r in range(r1, r2 + 1):
    temp = []
    for c in range(c1, c2 + 1):
        value = getValue(r, c)
        temp.append(value)
        maxLen = max(maxLen, len(str(value)))
    array.append(temp)

printFormat = str(maxLen)
for i in range(len(array)):
    for j in range(len(array[0])):
        if j < len(array[0]) - 1:
            print(format(array[i][j], printFormat), end=" ")
        else:
            print(format(array[i][j], printFormat))
