# 소수 판별 알고리즘

import math

# 기본 알고리즘 O(X)
# 시간복잡도 O(X)
def basic_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        True


# 제곱근까지만 확인
def basic_prime2(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        True
