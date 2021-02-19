# 백준 1654 랜선 자르기
# https://www.acmicpc.net/problem/1654
import sys

K, N = map(int, sys.stdin.readline().split())
lans = [int(sys.stdin.readline()) for _ in range(K)]

answer = 0
start, end = 1, max(lans)
while start <= end:
    mid = (start + end) // 2
    temp = sum([lan // mid for lan in lans])
    if temp >= N:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)