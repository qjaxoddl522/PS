import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    a, b = map(int, input().split())
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    q = deque([a])
    visited = [-1] * (N+1)
    visited[a] = 0

    while q:
        n = q.popleft()
        for nn in graph[n]:
            if visited[nn] == -1:
                visited[nn] = visited[n] + 1
                if nn == b:
                    print(visited[nn])
                    return
                q.append(nn)
    print(visited[b])
    
main()