import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque, defaultdict

def main():
    n, q = map(int, input().split())
    tree = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        if b != 1:
            tree[a].append(b)
        if a != 1:
            tree[b].append(a)
    ans_tree = [0]*(n+1)
    for _ in range(q):
        p, x = map(int, input().split())
        ans_tree[p] += x
    
    visited = set()
    que = deque()
    que.append(1)
    
    while que:
        current_top = que.popleft()
        visited.add(current_top)
        next_top = []
        while tree[current_top]:
            next_top.append(tree[current_top].pop())
        while next_top:
            check_visited = next_top.pop()
            if check_visited not in visited:
                tree[current_top].append(check_visited)
                que.append(check_visited)
                ans_tree[check_visited] += ans_tree[current_top]
    
    print(*ans_tree[1::])

def main2():
    n, q = map(int, input().split())
    tree = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        if b != 1:
            tree[a].append(b)
        if a != 1:
            tree[b].append(a)
    ans_tree = [0]*(n+1)
    for _ in range(q):
        p, x = map(int, input().split())
        ans_tree[p] += x
    
    visited = set()
    
    def dfs_recursive(current_top, cumlative_sum, visited):
        if current_top not in visited:
            visited.add(current_top)
            ans_tree[current_top] += cumlative_sum
            for next_top in tree[current_top]:
                dfs_recursive(next_top, ans_tree[current_top], visited)
    dfs_recursive(1, 0, visited)
    print(*ans_tree[1::])

main2()