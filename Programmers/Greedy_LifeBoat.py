def solution(people, limit):
    answer = 0
    pop = len(people)
    people.sort()
    h_cnt = 0
    t_cnt = -1
    while True:
        if h_cnt - t_cnt == pop + 1:
            break
        elif h_cnt - t_cnt == pop:
            answer += 1
            break
        if people[h_cnt] + people[t_cnt] > limit:
            answer += 1
            t_cnt -= 1
        else:
            answer += 1
            h_cnt += 1
            t_cnt -= 1

    return answer


import sys

people = list(map(int, sys.stdin.readline().split()))
limit = int(sys.stdin.readline())
print(f"결과는 {solution(people, limit)}입니다")
