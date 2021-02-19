# 백준 10825 정렬 국영수
# https://www.acmicpc.net/problem/10825
import sys

N = int(sys.stdin.readline())
sample = []
for _ in range(N):
    sample.append(tuple(sys.stdin.readline().split()))

sorted_sample = sorted(sample, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for sp in sorted_sample:
    print(sp[0])
