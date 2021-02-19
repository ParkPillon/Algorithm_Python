# 프로그래머스 정렬 H-index

citations = [10000] * 1000


def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    while answer < len(citations) and citations[answer] >= answer + 1:
        answer += 1
    return answer


print(solution(citations))