# 백준 1715번 카드 정렬하기 heapq 사용
# https://www.acmicpc.net/problem/1715
import sys
import heapq


N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    data = int(sys.stdin.readline())
    heapq.heappush(heap, data)

answer = 0
while len(heap) > 1:
    group1 = heapq.heappop(heap)
    group2 = heapq.heappop(heap)
    temp = group1 + group2
    answer += temp
    heapq.heappush(heap, temp)
print(answer)