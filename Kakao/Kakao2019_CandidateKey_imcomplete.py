# 카카오 2019 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890


relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
]

from collections import defaultdict


def solution(relation):
    answer = 0
    row, column = len(relation), len(relation[0])
    overlaps = [defaultdict(list) for _ in range(column)]
    for r in range(row):
        for c in range(column):
            value = relation[r][c]
            overlaps[c][value].append(r)
    print(overlaps)
    return answer


solution(relation)