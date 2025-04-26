import sys, math
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N, Q = map(int, input().split())
    A = [None] + list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 1번을 루트로 지정하고 한 번의 bfs로 깊이, 부모 구하기
    depth, parent = [0] * (N+1), [None] * (N+1)
    visited = [False] * (N+1)

    q = deque([(1, 0)])
    visited[1] = True
    while q:
        node, dep = q.popleft()
        for nextNode in graph[node]:
            if not visited[nextNode]:
                q.append((nextNode, dep+1))
                visited[nextNode] = True
                depth[nextNode] = dep + 1
                parent[nextNode] = node
    
    # 같은 깊이로 맞추고 두 노드의 루트까지 이동
    def GetPath(u, v):
        uPath = []
        vPath = []
        while depth[u] > depth[v]:
            uPath.append(u)
            u = parent[u]
        while depth[u] < depth[v]:
            vPath.append(v)
            v = parent[v]

        while u != v:
            uPath.append(u)
            vPath.append(v)
            u = parent[u]
            v = parent[v]
        vPath.reverse()
        
        return uPath + [u] + vPath

    MOD = 1000000007
    for _ in range(Q):
        start, end = map(int, input().split())
        result = 0
        for node in GetPath(start, end):
            power = int(math.log10(A[node])) + 1
            result = (result * pow(10, power, MOD) + A[node]) % MOD
        print(result)

main()