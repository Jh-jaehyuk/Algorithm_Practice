def solution(n, direction):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    x, y = 1, 1
    for i in direction:
        if i == 'R' and x != n:
            x += dx[2]
        elif i == 'L' and x != 1:
            x += dx[0]
        elif i == 'U' and y != 1:
            y += dy[1]
        elif i == 'D' and y != 5:
            y += dy[3]

    return y, x

n = int(input())
x, y = 1, 1
nx, ny = 0, 0
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny
print(x, y)
