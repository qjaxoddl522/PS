import sys
input = lambda: sys.stdin.readline().rstrip()

def Main():
    N = int(input())
    A = []
    B = []
    C = []
    D = []
    for _ in range(N):
        n, a, b, c, d = map(int, input().split())
        A.append((a, n))
        B.append((b, n))
        C.append((c, n))
        D.append((d, n))
    A.sort(key= lambda x: (-x[0], x[1]))
    B.sort(key= lambda x: (-x[0], x[1]))
    C.sort(key= lambda x: (-x[0], x[1]))
    D.sort(key= lambda x: (-x[0], x[1]))
    
    ans = []
    for ls in (A, B, C, D):
        i = 0
        while ls[i][1] in ans:
            i += 1
        ans.append(ls[i][1])
    print(*ans)

Main()