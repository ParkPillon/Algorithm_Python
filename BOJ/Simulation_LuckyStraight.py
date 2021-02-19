# 백준 18406
# https://www.acmicpc.net/problem/18406
import sys

N = sys.stdin.readline().strip()
idx_center = len(N) // 2
print(
    "LUCKY"
    if sum(map(int, N[:idx_center])) == sum(map(int, N[idx_center:]))
    else "READY"
)