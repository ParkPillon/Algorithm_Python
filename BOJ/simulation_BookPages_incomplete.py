# 백준 1019 책 페이지
# https://www.acmicpc.net/problem/1019

# https://www.slideshare.net/Baekjoon/baekjoon-online-judge-1019 참고
# N자리 수에 대해 (10**N-1 <= X < 10**N)
# 0: (9N-9)*(10**N-2)
# 나머지: (9N+1)*(10**N-2)
import sys

N = int(sys.stdin.readline())  # N이 n자리 정수라고 할 때


def countFreq(maxNum, frequency):  # n자리수 중 maxNum 이하인 수에 대해 숫자 빈도수 계산

    n = len(str(maxNum))
    first = maxNum // (10 ** (n - 1))  # 첫자리수
    for i in range(1, first):
        frequency[i] += 10 ** (n - 1)
        for j in range(10):
            frequency[j] += (n - 1) * (10 ** (n - 2))
    frequency[first] += maxNum % (10 ** (n - 1)) + 1


frequency = [0] * 10
if N < 10:
    for i in range(1, N + 1):
        frequency[i] += 1
else:
    for i in range(1, 10):
        frequency[i] += 1
    idx = 2  # 10페이지 부터 카운트
    while N // (10 ** idx):  # 10부터 99, 100부터 999 단위로 카운트
        frequency[0] += (9 * idx - 9) * (10 ** (idx - 2))
        for i in range(1, 10):
            frequency[i] += (9 * idx + 1) * (10 ** (idx - 2))
        idx += 1
    # n-1자리수 까지는 카운트 완료

print(*frequency)
