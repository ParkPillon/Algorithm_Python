# 카카오2020 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    answer = len(s)
    i = 1
    while i <= len(s) / 2:
        answer = min(answer, len(compress(s, i)))
        i += 1
    return answer


import sys


def compress(s, n):
    repeated = []
    for i in range(0, len(s), n):
        temp = s[i : i + n]

        if not repeated:  # 첫 문자열
            repeated.append([temp, 1])
            continue

        if temp != repeated[-1][0]:
            repeated.append([temp, 1])
        else:
            repeated[-1][1] += 1

    answer = ""
    for rep in repeated:
        if rep[1] != 1:
            answer += str(rep[1])
        answer += rep[0]
    return answer


s = sys.stdin.readline().strip()
print(f"정답은 {solution(s)}")
