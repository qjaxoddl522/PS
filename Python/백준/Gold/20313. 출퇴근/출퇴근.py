import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
    INF = int(1e19)
    N, M, A, B = map(int, input().split())
    edges = []
    base = []
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        u, v, t = map(int, input().split())
        edges.append((u, v))
        base.append(t)
        graph[u].append((v, i))
        graph[v].append((u, i))
    
    K = int(input())
    # W[k][i] = k번 사용 후 i번째 간선의 비용
    W = [base[:]]
    for _ in range(K):
        W.append(list(map(int, input().split())))
    
    final = [bytearray(K+1) for _ in range(N+1)]
    # dist[i][j] = i번째 노드에서 j번의 마법 사용했을 때 최단거리
    dist = [[INF]*(K+1) for _ in range(N+1)]
    dist[A][0] = 0
    hq = [(0, A, 0)]

    while hq:
        d, u, k = heappop(hq)
        if d != dist[u][k] or final[u][k]:
            continue
        final[u][k] = True
        
        for v, ei in graph[u]:
            if final[v][k]:
                continue
            w = W[k][ei]
            nd = d + w
            if nd < dist[v][k]:
                dist[v][k] = nd
                heappush(hq, (nd, v, k))
    
        if k < K and d < dist[u][k+1] and not final[u][k+1]:
            dist[u][k+1] = d
            heappush(hq, (d, u, k+1))

    ans = min(dist[B])
    print(ans)

main()