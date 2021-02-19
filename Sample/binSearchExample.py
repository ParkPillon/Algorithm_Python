# 이진탐색 샘플
"""
탐색범위가 큰 문제는 이진탐색으로 접근할 것
"""

# 재귀적 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# 반복문 구현
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# 파이썬 라이브러리 활용 bisect
from bisect import bisect_left, bisect_right


def count_by_range(array, left, right):
    right_idx = bisect_right(array, right)  # 우측 경계
    left_idx = bisect_left(array, left)  # 좌측 경계
    return right_idx - left_idx


# Parametric Search
"""
최적화 문제를 결정문제(예 아니오)로 바꾸어 해결하는 기법
특정한 조건을 만족할 경우 범위를 좁혀가는 방식
"""
