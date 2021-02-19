from itertools import permutations


def solution(numbers):
    answer = 0
    nums = []
    for i in range(1, len(numbers) + 1):
        nums += list(permutations(list(numbers), i))
    _nums = list(set([int("".join(num)) for num in nums]))
    for n in _nums:
        isPrime = True
        if n <= 1:
            continue
        for i in range(2, n):
            if n % i == 0:
                isPrime = False
                break
        if isPrime:
            answer += 1
    return answer


import sys

numbers = sys.stdin.readline().strip()
print(f"결과: {solution(numbers)}")