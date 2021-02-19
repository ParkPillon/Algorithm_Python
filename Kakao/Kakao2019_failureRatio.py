# 카카오 2019 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    f_list = []
    challengers = len(stages)  # 도전자 수
    for stage in range(1, N + 1):
        fail = stages.count(stage)
        fail_rate = fail / challengers if challengers else 0
        f_list.append((stage, fail_rate))
        challengers -= fail
    return [stage for stage, fail_rate in sorted(f_list, key=lambda x: -x[1])]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
