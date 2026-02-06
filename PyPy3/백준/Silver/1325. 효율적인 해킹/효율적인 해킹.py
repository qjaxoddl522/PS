import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[B].append(A)
    
    # 최대 해킹 수, 그 시작점들
    maxCon = 0
    ans = []
    for S in range(1, N+1):
        q = deque([S])
        visited = bytearray(N+1)
        visited[S] = True
        
        con = 1
        while q:
            node = q.popleft()
            for nNode in graph[node]:
                if not visited[nNode]:
                    con += 1
                    visited[nNode] = True
                    q.append(nNode)
        
        if con > maxCon:
            maxCon = con
            ans = [S]
        elif con == maxCon:
            ans.append(S)
    print(*sorted(ans))
    
main()