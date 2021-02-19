def solution(n, lost, reserve):

    # # 여벌 가져왔는데 도난
    # for l in range(len(lost)):
    #     if lost[l] in reserve:
    #         reserve.remove(lost[l])
    #         lost.remove(lost[l])
    # answer = n - len(lost)

    set_lost = set(lost)
    set_reserve = set(reserve)
    lost = list(set_lost - set_reserve)
    reserve = list(set_reserve - set_lost)
    answer = n - len(lost)
    # lost 탐색
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            answer += 1
            continue
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            answer += 1
            continue

    return answer


import sys

n = int(sys.stdin.readline())
lost = list(map(int, sys.stdin.readline().split()))
reserve = list(map(int, sys.stdin.readline().split()))

result = solution(n, lost, reserve)

print(f"{result}명이 체육수업을 들을 수 있습니다")
