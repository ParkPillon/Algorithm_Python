# 프로그래머스 힙 더맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        new_food = a + 2 * b
        heapq.heappush(scoville, new_food)
        answer += 1
    return answer


print(solution(scoville, K))