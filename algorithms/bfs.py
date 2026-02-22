from collections import deque

def bfs(start, graph):
    dist = [-1] * len(graph)
    dist[start] = 0
    que = deque([start])
    while que:
        v = que.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:      # 未訪問
                dist[nv] = dist[v] + 1
                que.append(nv)
    return dist