import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e10)
def main():
    for _ in range(int(input())):
        N, M, T = map(int, input().split())
        S, G, H = map(int, input().split())

        graph = [[] for _ in range(N+1)]
        ghw = None
        for _ in range(M):
            a, b, w = map(int, input().split())
            graph[a].append((b, w))
            graph[b].append((a, w))
            if (a == G and b == H) or (a == H and b == G):
                ghw = w if ghw is None else min(ghw, w)

        candidates = sorted(int(input()) for _ in range(T))
        
        def dijkstra(start):
            dist = [INF] * (N+1)
            dist[start] = 0
            visited = bytearray(N+1)
            hq = [(0, start)]
            while hq:
                d, u = heappop(hq)
                if visited[u]:
                    continue
                visited[u] = 1
                for v, w in graph[u]:
                    nd = d + w
                    if not visited[v] and dist[v] > nd:
                        dist[v] = nd
                        heappush(hq, (nd, v))
            return dist

        dS = dijkstra(S)
        dG = dijkstra(G)
        dH = dijkstra(H)

        ans = []
        for x in candidates:
            if dS[x] == INF:
                continue
            distGH = dS[G] + ghw + dH[x]
            distHG = dS[H] + ghw + dG[x]
            if dS[x] == distGH or dS[x] == distHG:
                ans.append(x)

        print(*ans)

main()