# 백준 15686 치킨 배달
# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations

# N, M = map(int, sys.stdin.readline().split())
# cityMap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
N, M = 5, 2
cityMap = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2],
]
house, store = [], []
for i in range(N):
    for j in range(N):
        if cityMap[i][j] == 1:
            house.append((i, j))
        elif cityMap[i][j] == 2:
            store.append((i, j))
candidates = list(combinations(store, M))
answer = 1e9


def distance(h_x, h_y, st_x, st_y):
    return abs(h_x - st_x) + abs(h_y - st_y)


def chickenRoad(h_x, h_y, stores):  # 한 집의 치킨거리
    answer = 1e9
    for st_x, st_y in stores:
        answer = min(answer, distance(h_x, h_y, st_x, st_y))
    return answer


for candidate in candidates:
    temp = 0
    for h_x, h_y in house:
        temp += chickenRoad(h_x, h_y, candidate)
    answer = min(answer, temp)

print(answer)