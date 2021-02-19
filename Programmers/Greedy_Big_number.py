def solution(number, k):
    answer = ""
    while k > 0:
        if len(number) == k:
            return answer
        if "9" in number[: k + 1]:
            selected = "9"
            selected_index = number.index(selected)
            answer += selected
            k -= selected_index
            number = number[selected_index + 1 :]
        else:
            selected = max(number[: k + 1])
            selected_index = number.index(selected)
            answer += selected
            k -= selected_index
            number = number[selected_index + 1 :]

    if k == 0:
        answer += number

    return answer


import sys

number = sys.stdin.readline().strip()
k = int(sys.stdin.readline())
print(f"결과: {solution(number,k)}")
