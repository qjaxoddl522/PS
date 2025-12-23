import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N = int(input())
    jump = [N] + list(map(int, input().split()))
    s, e = map(int, input().split())

    ndq = deque([s])
    visited = [False] * (N+1)
    for dist in range(1, N+1):
        dq = ndq
        ndq = deque()
        while dq:
            node = dq.popleft()
            interval = jump[node]
            for i in range(node + interval, N+1, interval):
                if not visited[i]:
                    visited[i] = True
                    ndq.append(i)
            for i in range(node - interval, 0, -interval):
                if not visited[i]:
                    visited[i] = True
                    ndq.append(i)
        if visited[e]:
            print(dist)
            break
    else:
        print(-1)

main()