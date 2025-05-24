import sys, math
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    A, B, C = map(int, input().split())
    MAX = A + B + C
    
    if MAX % 3 != 0:
        print(0)
        return

    visited = [[False] * (MAX+1) for _ in range(MAX+1)]
    visited[A][B] = True
    visited[B][A] = True

    def swap(n, m):
        if n > m:
            temp = n
            n = m
            m = temp
        return (n * 2, m - n)

    q = deque([(A, B)])
    while q:
        a, b = q.popleft()
        c = MAX - (a + b)

        if a == b and b == c:
            print(1)
            return
        
        for na, nb in (swap(a, b), swap(b, c), swap(c, a)):
            if visited[na][nb]:
                continue
            visited[na][nb] = True
            visited[nb][na] = True
            q.append((na, nb))
    print(0)

main()