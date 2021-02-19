# 선행스킬순서가 있고 여러가지의 스킬트리가 있을 때 가능한 스킬트리의 수


def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        _tree = "".join(
            [sk for sk in tree if sk in skill]
        )  # skill tree에서 선행스킬순서에 해당하는 스킬만 체크
        if not _tree:  # 조건에 해당하는 스킬이 없을 경우
            answer += 1
            continue
        if skill[: len(_tree)] == _tree:
            answer += 1

    return answer