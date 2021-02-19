# 백준 13549 숨바꼭질
# https://www.acmicpc.net/problem/1697
import sys
import heapq

INF = int(1e9)
N, K = map(int, sys.stdin.readline().split())
hq = []
heapq.heappush(hq, (0, N))
find_time = [INF] * 100001
find_time[N] = 0
while hq:
    time, now = heapq.heappop(hq)
    if now == K:
        print(time)
        break
    if now + 1 <= 100000 and time + 1 < find_time[now + 1]:
        heapq.heappush(hq, (time + 1, now + 1))
        find_time[now + 1] = time + 1
    if now - 1 >= 0 and time + 1 < find_time[now - 1]:
        heapq.heappush(hq, (time + 1, now - 1))
        find_time[now - 1] = time + 1
    if now * 2 <= 100000 and time < find_time[now * 2]:
        heapq.heappush(hq, (time + 1, now * 2))
        find_time[now * 2] = time
