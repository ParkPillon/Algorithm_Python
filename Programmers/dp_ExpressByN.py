# 프로그래머스 N으로 표현
# https://programmers.co.kr/questions/14645

N = 5
number = 12


def solution(N, number):
    if N == number:
        return 1
    sample = [{}]
    sample.append({N})
    for i in range(2, 9):  # i개로 만들 수 있는 숫자들 i:2~8
        a = set()
        a.add(int(str(N) * i))  # 5가 반복되는 수
        for k in range(1, i // 2 + 1):  # 4회의 경우 = (1회, 1회) + (2회, 2회) 연산상대는 i-k
            for operand1 in sample[k]:
                for operand2 in sample[i - k]:
                    print(f"{operand1}, {operand2}에 대해")
                    a.add(operand1 + operand2)
                    a.add(operand1 - operand2)
                    a.add(operand2 - operand1)
                    a.add(operand1 * operand2)
                    if operand1:
                        a.add(operand2 // operand1)
                    if operand2:
                        a.add(operand1 // operand2)
        sample.append(a)
        print(sample)
        if number in a:
            return i

    return -1


print(solution(N, number))
