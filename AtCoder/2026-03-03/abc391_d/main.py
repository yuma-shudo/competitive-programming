import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
    n, w = map(int, input().split())
    blocks = defaultdict(list)
    for i in range(1, n+1):
        x, y = map(int, input().split())
        blocks[x].append((y, i))
    min_block = float('inf')
    for i in range(1, w+1):
        blocks[i].sort()
        min_block = min(min_block, len(blocks[i]))
    disappear = [float('inf')] * (n+1)
    for i in range(min_block):
        max_height = 0
        for j in range(1, w+1):
            max_height = max(max_height, blocks[j][i][0])
        for j in range(1, w+1):
            disappear[blocks[j][i][1]] = max_height
    q = int(input())
    for _ in range(q):
        t, a = map(int ,input().split())
        if t+0.5<disappear[a]:
            print("Yes")
        else:
            print("No")

main()