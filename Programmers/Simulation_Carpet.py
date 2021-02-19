def solution(brown, yellow):
    answer = []
    sample = []
    for i in range(1, int((brown + yellow) ** 0.5) + 1):
        if (brown + yellow) % i == 0:
            sample.append([(brown + yellow) // i, i])

    answer = [sp for sp in sample if ((sp[0] - 1) + (sp[1] - 1)) * 2 == brown]
    return answer[0]


import sys

brown = int(sys.stdin.readline())
yellow = int(sys.stdin.readline())
print(f"결과는 {solution(brown, yellow)}")
