# 백준 20540 연길이의 이상형
# https://www.acmicpc.net/problem/20540

import sys

mbti = list(sys.stdin.readline().strip())
if mbti[0] == "E":
    mbti[0] = "I"
else:
    mbti[0] = "E"
if mbti[1] == "S":
    mbti[1] = "N"
else:
    mbti[1] = "S"
if mbti[2] == "T":
    mbti[2] = "F"
else:
    mbti[2] = "T"
if mbti[3] == "J":
    mbti[3] = "P"
else:
    mbti[3] = "J"

print("".join(mbti))
