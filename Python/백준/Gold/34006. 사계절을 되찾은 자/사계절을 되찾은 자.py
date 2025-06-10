import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N = int(input())
    A, B, C = map(int, input().split())
    a, b, c = map(int, input().split())

    # prev[i][j] = A가 i이고 B가 j일 때 이전의 공격 (0:궁기, 1:도올, 2:혼돈)
    # C의 경우 3N - A - B를 통해 알 수 있음
    prev = [[-1] * (N * 2 + 1) for _ in range(N * 2 + 1)]
    prev[A][B] = None

    q = deque([(A, B)])
    while q:
        aa, bb = q.popleft()
        if aa == N and bb == N:
            break
        cc = N * 3 - aa - bb

        # 궁기
        if aa + a < N * 2 and cc - a > 0 and prev[aa + a][bb] == -1:
            prev[aa + a][bb] = 0
            q.append((aa + a, bb))
        # 도올
        if bb + b < N * 2 and aa - b > 0 and prev[aa - b][bb + b] == -1:
            prev[aa - b][bb + b] = 1
            q.append((aa - b, bb + b))
        # 혼돈
        if cc + c < N * 2 and bb - c > 0 and prev[aa][bb - c] == -1:
            prev[aa][bb - c] = 2
            q.append((aa, bb - c))
    
    if prev[N][N] == -1:
        print(-1)
        return
    
    # 역추적
    path = []
    pa, pb = N, N
    while prev[pa][pb] != None:
        p = prev[pa][pb]
        if p == 0:
            path.append('A')
            pa = pa - a
        elif p == 1:
            path.append('B')
            pa, pb = pa + b, pb - b
        elif p == 2:
            path.append('C')
            pb = pb + c
    
    print(len(path))
    print(*reversed(path), sep='')

main()