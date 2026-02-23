import heapq
from collections import defaultdict

def dijkstra(start, graph, n):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (コスト, 頂点)

    while heap:
        cost, v = heapq.heappop(heap)
        if cost > dist[v]:   # すでに最短経路が確定済み
            continue
        for nv, weight in graph[v]:
            new_cost = dist[v] + weight
            if new_cost < dist[nv]:
                dist[nv] = new_cost
                heapq.heappush(heap, (new_cost, nv))

    return dist