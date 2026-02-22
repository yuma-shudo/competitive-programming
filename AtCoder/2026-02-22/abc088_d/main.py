import sys
input = sys.stdin.readline
from collections import deque

def main():
    h, w = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(h)]
    ans = [[-1]*w for _ in range(h)]

    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    que = deque()
    que.append((0, 0))
    ans[0][0] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if ans[nx][ny] != -1 or grid[nx][ny] == "#":
                continue
                
            ans[nx][ny] = ans[x][y] + 1
            que.append((nx, ny))
    
    black_square = 0
    for row in grid:
        black_square += row.count("#")
    print(h*w - (ans[h-1][w-1] + black_square) if ans[h-1][w-1] != -1 else -1)

main()