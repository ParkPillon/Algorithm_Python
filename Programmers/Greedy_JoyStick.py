def solution(name):
    answer = 0
    ord_name = [min(ord(n) - 65, 91 - ord(n)) for n in name]
    print(ord_name)
    where = 0
    while True:
        answer += ord_name[where]
        ord_name[where] = 0
        if sum(ord_name) == 0:
            break
        # 가장 가까운 수정지점 체크 (우측, 좌측)
        temp_r = where + 1
        while temp_r < len(ord_name) and ord_name[temp_r] == 0:
            temp_r += 1
        r_dis = temp_r - where
        temp_l = where - 1
        while temp_l >= -len(ord_name) and ord_name[temp_l] == 0:
            temp_l -= 1
        l_dis = where - temp_l
        if r_dis <= l_dis:
            where = temp_r
            answer += r_dis
        else:
            where = temp_l
            answer += l_dis
        print(f"{ord_name} answer:{answer}, where:{where}")
    return answer


import sys

name = sys.stdin.readline().strip()
print(f"결과는 {solution(name)}입니다")
