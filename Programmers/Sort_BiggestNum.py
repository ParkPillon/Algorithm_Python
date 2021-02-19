# 프로그래머스 정렬 가장 큰 수


def sortKey(number):  # numbers 정렬하는 조건 key
    strNum = str(number)
    # if len(strNum) == 1:
    #     key = int(strNum * 4)
    # elif len(strNum) == 2:
    #     key = int(strNum * 2)
    # elif len(strNum) == 3:
    #     key = int(strNum + strNum[0])
    # else:
    #     key = int(strNum)
    key = strNum * 3
    print(key)
    return key


def solution(numbers):
    answer = ""
    numbers.sort(key=lambda num: sortKey(num))
    for num in numbers:
        answer += str(num)
    return str(int(answer))


numbers = [1000, 100, 10, 0]
print(solution(numbers))

"""
좋은 풀이 
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
"""
