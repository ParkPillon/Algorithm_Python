# 백준 10815 숫자 카드
# https://www.acmicpc.net/problem/10815

import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(sys.stdin.readline())
samp = list(map(int, sys.stdin.readline().split()))


def count_by_range(array, left, right):
    right_idx = bisect_right(array, right)  # 우측 경계
    left_idx = bisect_left(array, left)  # 좌측 경계
    return right_idx - left_idx


answer = [count_by_range(cards, s, s) for s in samp]
print(*answer)
