# 카카오 2020 가사검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

import sys

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

from bisect import bisect_left, bisect_right


def count_by_range(array, left, right):
    right_idx = bisect_right(array, right)  # 우측 경계
    left_idx = bisect_left(array, left)  # 좌측 경계
    return right_idx - left_idx


def solution(words, queries):
    answer = []
    sample = {}  # 길이별 단어
    sample_reversed = {}
    for word in words:
        length = len(word)
        if length in sample:
            sample[length].append(word)
        else:
            sample[length] = [word]
        if length in sample_reversed:
            sample_reversed[length].append(word[::-1])
        else:
            sample_reversed[length] = [word[::-1]]

    # 단어 정렬
    for value in sample.values():
        value.sort()
    for value in sample_reversed.values():
        value.sort()

    for keyword in queries:
        length = len(keyword)
        count = 0
        if length not in sample:
            answer.append(0)
            continue
        if keyword[0] != "?":
            count = count_by_range(
                sample[length], keyword.replace("?", "a"), keyword.replace("?", "z")
            )
        else:
            count = count_by_range(
                sample_reversed[length],
                keyword[::-1].replace("?", "a"),
                keyword[::-1].replace("?", "z"),
            )
        answer.append(count)
    return answer


print(solution(words, queries))