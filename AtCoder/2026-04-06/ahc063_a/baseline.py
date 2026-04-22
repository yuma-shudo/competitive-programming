import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())
d = list(map(int, input().split()))
f = [list(map(int, input().split())) for _ in range(N)]

ans = []

for _ in range(4, N - 1):
    ans.append('D')

for col in range(1, N):
    ans.append('R')
    if col % 2 == 1:
        for _ in range(N - 2):
            ans.append('U')
    else:
        for _ in range(N - 2):
            ans.append('D')

ans.append('U')

for _ in range(N - 1):
    ans.append('L')

print('\n'.join(ans))
