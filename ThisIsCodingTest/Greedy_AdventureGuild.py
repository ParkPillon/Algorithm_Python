# 이코테 알고리즘 기출문제 Q.01

import sys

N = int(sys.stdin.readline())
fear_value = list(map(int, sys.stdin.readline().split()))
fear_value.sort()
member = 0
group = 0
for value in fear_value:
    member += 1
    if member == value:
        group += 1
        member = 0
    elif value > member:
        continue
print(group)