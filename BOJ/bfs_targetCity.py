# 백준 18352 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

import sys
from collections import deque

answers = []
N, M, K, X = map(int, sys.stdin.readline().split())
roads = [list(map(int, sys.stdin.readline().split())) for m in range(M)]
_roads = {}
for rd in roads:
    if rd[0] in _roads:
        _roads[rd[0]].append(rd[1])
    else:
        _roads[rd[0]] = [rd[1]]

queue = deque([X])
distance = {X: 0}
while queue:
    temp = queue.popleft()
    if temp in _roads:
        for i in _roads[temp]:
            if i in distance:
                continue
            queue.append(i)
            distance[i] = distance[temp] + 1

for key in sorted(distance.keys()):
    if distance[key] == K:
        answers.append(key)
if answers:
    for ans in answers:
        print(ans)
else:
    print(-1)