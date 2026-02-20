import sys
input = sys.stdin.readline
from collections import deque

def main():
    try:
        h, w = map(int, input().split())
        grid = [list(input()) for _ in range(h)]
    except ValueError:
        return
    
    visited = [[-1]*w for _ in range(h)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))
    ans = 1

    directions = [(1, 0), (0, 1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if nx < h and ny < w:
                if visited[nx][ny] == -1 and grid[nx][ny] != "#":
                    steps = visited[x][y]+1
                    ans = max(ans, steps)
                    visited[nx][ny] = steps
                    q.append((nx, ny))
    
    print(ans)

def main2():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    
    dp = [[0]*w for _ in range(h)]
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if grid[i][j] == "#":
                continue
            right = dp[i][j+1] if j+1 < w else 0
            below = dp[i+1][j] if i+1 < h else 0
            dp[i][j] = max(right, below) + 1
    
    print(dp[0][0])

main2()