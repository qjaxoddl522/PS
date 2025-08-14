import sys, math
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
    N = int(input())
    
    graph = [[] for _ in range(N+1)]
    inner = [0] * (N+1)
    time = [0]

    for i in range(1, N+1):
        inp = list(map(int, input().split()))
        for j in inp[2:]:
            graph[j].append(i)
        inner[i] += inp[1]
        time.append(inp[0])
    
    answer = 0
    hq = []
    for i in range(1, N+1):
        if inner[i] == 0:
            heappush(hq, [time[i], i])
    while hq:
        t, idx = heappop(hq)
        answer += t

        if t > 0:
            for i in range(len(hq)):
                hq[i][0] -= t
        
        for next in graph[idx]:
            inner[next] -= 1
            if inner[next] == 0:
                heappush(hq, [time[next], next])
    print(answer)

main()