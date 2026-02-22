graph = {0: [1, 2], 1: [3], 2: [3], 3: []}

# ① 再帰版
def dfs_recursive(v, visited):
    visited.add(v)
    for nv in graph[v]:
        if nv not in visited:
            dfs_recursive(nv, visited)

# ② スタック版（再帰を使わない）
def dfs_stack(start):
    visited = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        for nv in graph[v]:
            if nv not in visited:
                stack.append(nv)