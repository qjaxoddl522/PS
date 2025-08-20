import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
    for _ in range(int(input())):
        n, d, c = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((a, s))
        
        time = [float('inf')] * (n+1)
        visited = [False] * (n+1)
        
        hq = [(0, c)]
        time[c] = 0
        while hq:
            s, a = heappop(hq)
            if visited[a]:
                continue
            visited[a] = True
            
            for na, ns in graph[a]:
                if visited[na]:
                    continue
                if time[na] > s + ns:
                    time[na] = s + ns
                    heappush(hq, (s + ns, na))
        
        num = 0; t = 0
        for i in range(n+1):
            if visited[i]:
                num += 1
                t = max(t, time[i])
        print(num, t)

main()