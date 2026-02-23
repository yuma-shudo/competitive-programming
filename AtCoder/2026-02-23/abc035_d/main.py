import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

def main():
    n, m, t = map(int, input().split())
    prize = list(map(int, input().split()))
    town_graph = defaultdict(list)
    r_town_graph = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, input().split())
        town_graph[a].append((b, c))
        r_town_graph[b].append((a, c))

    def djikstra(heap, graph, min_cost):
        while heap:
            cost, vertex = heapq.heappop(heap)
            if cost > min_cost[vertex]:
                continue
            for nvertex, add_cost in graph[vertex]:
                new_cost = cost + add_cost
                if new_cost < min_cost[nvertex]:
                    min_cost[nvertex] = new_cost
                    heapq.heappush(heap, (min_cost[nvertex], nvertex))
        return min_cost
    cost = [float('inf') for _ in range(n+1)]
    cost[1] = 0
    heap = [(0, 1)]
    for_cost = djikstra(heap, town_graph, cost)
    cost = [float('inf') for _ in range(n+1)]
    cost[1] = 0
    heap = [(0, 1)]
    back_cost = djikstra(heap, r_town_graph, cost)
    ans = 0
    for i in range(n):
        ans = max(ans, (t - (for_cost[i+1] + back_cost[i+1])) * prize[i])
    print(ans)

main()