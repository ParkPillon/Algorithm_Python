import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# N = int(sys.stdin.readline())
# K = int(sys.stdin.readline())
# apples = [
#     (int(a[0]) - 1, int(a[1]) - 1)
#     for a in [sys.stdin.readline().split() for _ in range(K)]
# ]
# L = int(sys.stdin.readline())
# veer = {int(a[0]): a[1] for a in [sys.stdin.readline().split() for _ in range(L)]}

N = 10
K = 5
apples = [(0, 4), (0, 2), (0, 1), (0, 5), (0, 6)]
L = 4
veer = {8: "D", 10: "D", 11: "D", 13: "L"}

state = [(0, 0, 0)]


def solution():
    time = 0
    while True:
        time += 1
        try:
            if time in veer:  # 방향전환할 경우
                move(veer[time])
            else:
                move()
        except:
            print("부딪혔습니다")
            print(time)
            break


def move(turn=None):
    global state
    last_pos = state[-1][0], state[-1][1]
    direction = state[-1][2]
    new_pos = last_pos[0] + dx[direction], last_pos[1] + dy[direction]
    if (
        new_pos[0] < 0
        or new_pos[0] >= N
        or new_pos[1] < 0
        or new_pos[1] >= N
        or new_pos in [(s[0], s[1]) for s in state]
    ):
        raise Exception()
    if turn == "L":
        direction = (direction + 1) if direction < 3 else (3 - direction)
    elif turn == "D":
        direction = (direction - 1) if direction > 0 else (3 - direction)
    # 사과가 있는 경우
    if new_pos in apples:
        apples.remove(new_pos)
    else:
        state = state[1:]
    state.append((new_pos[0], new_pos[1], direction))
    print(state)


solution()