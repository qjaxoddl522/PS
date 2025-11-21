import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    def compare(x1, y1, x2, y2, d):
        return (x2 - x1) ** 2 + (y2 - y1) ** 2 <= d ** 2
    
    def getDist(start):
        visited = bytearray(N)
        visited[start] = True
        q = deque([(start, 0)])
        while q:
            node, dist = q.popleft()
            if canAttack[node]:
                return dist

            for next in graph[node]:
                if not visited[next]:
                    visited[next] = True
                    q.append((next, dist+1))
        return -1

    N, R, D, X, Y = map(int, input().split())
    tower = [tuple(map(int, input().split())) for _ in range(N)]

    canAttack = bytearray(N)
    graph = [[] for _ in range(N)]
    for i in range(N):
        x, y = tower[i][0], tower[i][1]
        if compare(x, y, X, Y, R):
            canAttack[i] = True
        for j in range(i):
            if compare(x, y, tower[j][0], tower[j][1], R):
                graph[i].append(j)
                graph[j].append(i)
    
    ans = 0.0
    for i in range(N):
        if canAttack[i]:
            ans += D
            continue
        DD = D
        dist = getDist(i)
        if dist > 0:
            for _ in range(dist):
                DD /= 2
            ans += DD
    print(ans)

main()