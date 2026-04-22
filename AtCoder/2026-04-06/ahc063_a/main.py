import sys
from collections import deque
input = sys.stdin.readline

N, M, C = map(int, input().split())
d = list(map(int, input().split()))
f = [list(map(int, input().split())) for _ in range(N)]

ans = []
colors = deque([1, 1, 1, 1, 1])
snake_length = 5

def eat(nr, nc):
    global snake_length
    if f[nr][nc] > 0:
        colors.append(f[nr][nc])
        f[nr][nc] = 0
        snake_length += 1

def do_move(direction, nr, nc):
    ans.append(direction)
    eat(nr, nc)

def bite_off_row0(buf_size):
    for j in range(buf_size - 1, -1, -1):
        f[0][j] = colors.pop()

# フェーズ1: 蛇行で全餌収集
r, c = 4, 0
for _ in range(4, N - 1):
    r += 1
    do_move('D', r, c)

for col in range(1, N):
    c += 1
    do_move('R', r, c)
    if col % 2 == 1:
        for _ in range(N - 2):
            r -= 1
            do_move('U', r, c)
    else:
        for _ in range(N - 2):
            r += 1
            do_move('D', r, c)

r -= 1
do_move('U', r, c)
for _ in range(N - 1):
    c -= 1
    do_move('L', r, c)

# r=0, c=0

# フェーズ2
r += 1
do_move('D', r, c)

buf_size = N
remaining = M - N - 1

if remaining % 2 == 1:
    remaining += 1
    buf_size = N - 1

while r < N - 2:
    back_cost = r + 1
    if remaining <= back_cost + 1:
        break
    r += 1
    do_move('D', r, c)
    remaining -= 1

going_right = True

while True:
    if going_right:
        back_cost = r + 1 if c == 0 else c + r
        if remaining <= back_cost:
            break
        if c < N - 2:
            do_move('R', r, c + 1)
            c += 1
            remaining -= 1
            if c == N - 2:
                do_move('U', r - 1, c)
                r -= 1
                remaining -= 1
                going_right = False
        else:
            do_move('U', r - 1, c)
            r -= 1
            remaining -= 1
            going_right = False
    else:
        back_cost = c + r - 1
        if remaining <= back_cost:
            break
        if c > 1:
            do_move('L', r, c - 1)
            c -= 1
            remaining -= 1
            if c == 1:
                do_move('U', r - 1, c)
                r -= 1
                remaining -= 1
                going_right = True
        else:
            do_move('U', r - 1, c)
            r -= 1
            remaining -= 1
            going_right = True

if going_right:
    if c == 0:
        do_move('R', r, c + 1)
        c += 1
        while r > 1:
            do_move('U', r - 1, c)
            r -= 1
        do_move('L', r, c - 1)
        c -= 1
    else:
        do_move('U', r - 1, c)
        r -= 1
        while c > 1:
            do_move('L', r, c - 1)
            c -= 1
        while r > 1:
            do_move('U', r - 1, c)
            r -= 1
        do_move('L', r, c - 1)
        c -= 1
else:
    while c > 1:
        do_move('L', r, c - 1)
        c -= 1
    while r > 1:
        do_move('U', r - 1, c)
        r -= 1
    do_move('L', r, c - 1)
    c -= 1

# r=1, c=0、噛みちぎり発動
bite_off_row0(buf_size)

# フェーズ3
def go_to_start():
    global r, c
    for _ in range(N - 2):
        do_move('D', r + 1, c)
        r += 1

def eat_and_return(eat_col):
    global r, c
    while r > 0:
        do_move('U', r - 1, c)
        r -= 1
    do_move('L', r, c - 1)
    c -= 1
    do_move('D', r + 1, c)
    r += 1
    while c > 0:
        do_move('L', r, c - 1)
        c -= 1
    go_to_start()

# (1,0)からD×(N-2)で出発点(N-1,0)へ
go_to_start()

eat_row = 2 if N % 2 == 0 else 1

# bite_off後のsnake_lengthを調整
snake_length -= buf_size  # 噛みちぎりでbuf_size個減る

while snake_length < M:
# for _ in range(5):
    want_color = d[snake_length]  # 次に食べたい色

    going_right = True
    first = True
    while r != eat_row:
        if going_right:
            steps = N - 1 if first else N - 2
            first = False
            for _ in range(steps):
                do_move('R', r, c + 1)
                c += 1
            do_move('U', r - 1, c)
            r -= 1
            going_right = False
        else:
            for _ in range(N - 2):
                do_move('L', r, c - 1)
                c -= 1
            do_move('U', r - 1, c)
            r -= 1
            going_right = True

    remaining_food = buf_size - (snake_length - (M - buf_size))
    target_col = None
    fallback_col = None
    for j in range(buf_size - 1, 0, -1):
        if f[0][j] > 0:
            if f[0][j] == want_color and target_col is None:
                target_col = j
            elif fallback_col is None:
                fallback_col = j

    eat_col = target_col if target_col is not None else fallback_col

    if eat_col is not None:
        while c > eat_col:
            do_move('L', r, c - 1)
            c -= 1
        eat_and_return(eat_col)
    else:
        while c > 1:
            do_move('L', r, c - 1)
            c -= 1
        while r > 1:
            do_move('U', r - 1, c)
            r -= 1
        do_move('U', r - 1, c)
        r -= 1
        do_move('L', r, c - 1)
        c -= 1
        do_move('D', r + 1, c)
        r += 1
        go_to_start()

print('\n'.join(ans))