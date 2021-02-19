# 백준 1062 가르침
# https://www.acmicpc.net/problem/1062

import sys

N, K = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(N)]

learned = [0] * 26
learned[ord("a") - 97] = 1
learned[ord("n") - 97] = 1
learned[ord("t") - 97] = 1
learned[ord("i") - 97] = 1
learned[ord("c") - 97] = 1


def dfs(count, last):
    global maxWords
    if count == K:
        answer = 0
        for word in words:
            possible = True
            for ch in word:
                if not learned[ord(ch) - 97]:  # 배우지 않은 문자
                    possible = False
                    break
            if possible:
                answer += 1
        maxWords = max(maxWords, answer)
    for ch in range(26):
        if ch <= last:
            continue
        if learned[ch]:
            continue
        learned[ch] = 1
        dfs(count + 1, ch)
        learned[ch] = 0


if K < 5:
    print(0)
else:
    maxWords = 0
    dfs(5, -1)
    print(maxWords)
