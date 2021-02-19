# 이코테 특정 수의 개수 구하기
# Zoho 인터뷰
import sys
from bisect import bisect_left, bisect_right

N, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))


def count_by_range(array, left, right):
    right_idx = bisect_right(array, right)  # 우측 경계
    left_idx = bisect_left(array, left)  # 좌측 경계
    return right_idx - left_idx


count = count_by_range(array, x, x)
print(count if count else -1)
