import sys
from collections import Counter

# 기본 입력
n = int(sys.stdin.readline())

# 띄어쓰기로 구분된 숫자 두개 입력받기. n개에도 적용가능
a, b = map(int, sys.stdin.readline().split())

# 띄어쓰기로 구분된 숫자들 list로 그대로 받음
inputList = list(map(int, sys.stdin.readline().split()))

# n줄에 걸쳐서 숫자n개를 [1, 2, 3 ... n]으로 입력
sample = [int(sys.stdin.readline()) for i in range(n)]

# n행 ?열의 2차원 행렬 입력받기
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# lost와 reserve 두 리스트에서 서로 중복되는 값을 제거 (set 이용 가능)
reserve = [1, 2, 3, 4]
lost = [2, 3, 4, 5]
_reserve = [r for r in reserve if r not in lost]
_lost = [l for l in lost if l not in reserve]

# 2차원 방향벡터를 이용
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# DFS / BFS 에 Stack과 Queue 사용
# Stack은 list, Que는 collections.deque 사용
# Que에 list사용 시 시간복잡도 증가

# Factorial
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


# Euclidean algorithm
def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


# rotate arr 90degree
def rotate90d(arr, k):
    m, n = len(arr), len(arr[0])
    if k == 0:
        return arr
    if k == 1:
        new_arr = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_arr[n - j - 1][i] = arr[i][j]
        return new_arr
    return rotate90d(rotate90d(arr, k - 1), 1)


# 원형의 경우 길이를 두배로 늘여서 일자형으로 풀어서 생각하면 편해짐

# 중복된 값을 줄여주어 반복문 연산 횟수도 줄어듬
new_counter = Counter("abbcccdddd")
# Counter({'d':4, 'c':3, 'b':2, 'a':1})


# list 출력 시
aList = [1, 2, 3]
print(*aList)  # 공백간격두고 출력됨

# [1,2,3,4,5,6] 배열을 두 그룹으로 분할할 때 (3개, 3개)
# [2,3,4,5,6]에 대해 5C3을 수행하면
# 중복되는 분할 없음
# 6C3의 경우 (1,3,5)와 (2,4,6)이 중복
