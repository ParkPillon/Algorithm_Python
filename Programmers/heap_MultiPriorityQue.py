# 프로그래머스 힙 이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

operations = ["I 16", "D 1"]

import heapq


def solution(operations):
    answer = []
    minQueue = []
    maxQueue = []
    for op in operations:
        command, num = op.split()
        if command == "I":
            heapq.heappush(minQueue, int(num))
            heapq.heappush(maxQueue, -int(num))
        else:
            if not minQueue:  # 비어있을 경우
                continue
            if num == "-1":  # 최소값 삭제
                result = heapq.heappop(minQueue)
                maxQueue.remove(-result)
                heapq.heapify(maxQueue)
            else:  # 최대값 삭제
                result = -heapq.heappop(maxQueue)
                minQueue.remove(result)
                heapq.heapify(minQueue)
    if minQueue:
        answer = [-heapq.heappop(maxQueue), heapq.heappop(minQueue)]
    else:
        answer = [0, 0]
    return answer


print(solution(operations))
