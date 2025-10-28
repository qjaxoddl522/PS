import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def Main():
    MAX = int(1e9)
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for w in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
    S, E = map(int, input().split())
    
    hq = [(-MAX, S)]
    visited = bytearray(N+1)
    weight = [0] * (N+1)
    while hq:
        w, node = heappop(hq)
        if visited[node]:
            continue
        visited[node] = True
        weight[node] = -w

        for nnode, nw in graph[node]:
            if not visited[nnode]:
                # 감당가능한 최대 중량을 힙큐에 입력
                heappush(hq, (max(w, -nw), nnode))
    print(weight[E])

Main()