# 프로그래머스 힙 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627

jobs = [
    [24, 10],
    [28, 39],
    [43, 20],
    [37, 5],
    [47, 22],
    [20, 47],
    [15, 34],
    [15, 2],
    [35, 43],
    [26, 1],
]

import heapq
from collections import deque


def solution(jobs):
    jobs.sort()
    answer = 0
    start_time = 0
    queue = deque(jobs)
    hq = []  # 가능한 작업 목록
    while queue or hq:
        print(queue)
        while queue and queue[0][0] <= start_time:  # 현재 시점에 가능한 작업을 heapq에 삽입
            requested_time, duration = queue.popleft()
            heapq.heappush(hq, (duration, requested_time))
        if not hq:  # 가능한 작업이 없을 때
            start_time += 1
            continue
        selected = heapq.heappop(hq)
        waiting = start_time - selected[1] + selected[0]  # 요청한 시각부터 끝난 시각까지의 시간
        answer += waiting
        start_time += selected[0]
    answer = answer // len(jobs)
    return answer


print(solution(jobs))