# 프로그래머스 단어변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]

from collections import deque


def solution(begin, target, words):
    answer = 0
    N = len(words)
    visited = [0] * N
    count = 0
    queue = deque([(begin, count)])
    while queue:
        word, c = queue.popleft()
        for i in range(N):
            if not visited[i] and isConvertible(word, words[i]):
                if words[i] == target:
                    answer = c + 1
                queue.append((words[i], c + 1))
                visited[i] = 1
    return answer


def isConvertible(word, target):
    if len(word) != len(target):
        return False
    difference = 0
    for a, b in zip(word, target):
        if a != b:
            difference += 1
    return True if difference == 1 else False


print(solution(begin, target, words))