# 이코테 이진탐색 부품 찾기
import sys

N = int(sys.stdin.readline())
parts = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
needs = list(map(int, sys.stdin.readline().split()))


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


for need in needs:
    if binary_search(parts, need, 0, N - 1) != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
