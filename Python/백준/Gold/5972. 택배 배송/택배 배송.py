import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, plusc = map(int, input().split())
        graph[a].append((b, plusc))
        graph[b].append((a, plusc))
    
    visited = bytearray(N+1)
    cost = [float('inf')] * (N+1)
    cost[1] = 0
    hq = [(0, 1)]
    while hq:
        c, node = heappop(hq)
        if visited[node]:
            continue
        visited[node] = True

        for next, plusc in graph[node]:
            if visited[next]:
                continue
            if cost[next] > c + plusc:
                cost[next] = c + plusc
                heappush(hq, (cost[next], next))
    print(cost[N])

main()