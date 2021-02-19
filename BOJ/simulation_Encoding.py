# 백준 1759 암호 만들기
# https://www.acmicpc.net/problem/1759

import sys
from itertools import combinations

VOWEL = ["a", "e", "i", "o", "u"]
L, C = map(int, sys.stdin.readline().split())
candidates = sys.stdin.readline().split()

v_letters = [l for l in candidates if l in VOWEL]
c_letters = [l for l in candidates if l not in VOWEL]
answer = []
for i in range(1, L - 1):  # 암호에 사용된 모음 수
    j = L - i  # 암호에 사용된 자음 수

    if i > len(v_letters) or j > len(c_letters):
        continue
    for v_combi in combinations(v_letters, i):
        for c_combi in combinations(c_letters, j):
            word = list(v_combi) + list(c_combi)
            word.sort()
            answer.append("".join(word))
answer.sort()
for a in answer:
    print(a)