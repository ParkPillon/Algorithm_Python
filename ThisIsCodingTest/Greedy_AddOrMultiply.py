import sys

S = list(map(int, sys.stdin.readline().strip()))
answer = 0
for number in S:
    answer = max(answer + number, answer * number)

print(answer)