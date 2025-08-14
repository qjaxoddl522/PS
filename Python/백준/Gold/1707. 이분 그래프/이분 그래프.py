import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    for _ in range(int(input())):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V)]

        for _ in range(E):
            u, v = map(int, input().split())
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        def bfs(start):
            q = deque([(start, 0)])
            dist[start] = 0
            while q:
                cur, d = q.popleft()
                for next in graph[cur]:
                    if dist[next] == -1:
                        dist[next] = d + 1
                        q.append((next, d + 1))
                    elif dist[next] % 2 == d % 2:
                        return False
            return True

        dist = [-1] * V
        for p in range(V):
            if dist[p] == -1:
                if not bfs(p):
                    print("NO")
                    break
        else:
            print("YES")

main()