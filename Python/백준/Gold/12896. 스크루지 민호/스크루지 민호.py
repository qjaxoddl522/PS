import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
트리의 지름을 구한 후 절반에 올림하면 최대를 최소화한 거리
"""
def Main():
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    def GetFar(start):
        q = deque([(start, 0)])
        visited = [False] * (N+1)
        visited[start] = True
        while q:
            node, dist = q.popleft()
            for next in graph[node]:
                if not visited[next]:
                    q.append((next, dist+1))
                    visited[next] = True
        return node, dist
    
    rad = GetFar(GetFar(1)[0])[1]
    print((rad + 1) // 2)

Main()