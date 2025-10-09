import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    move = ((0,1),(0,-1),(1,0),(-1,0))
    N, M, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [bytearray(M) for _ in range(N)]
    visited[0][0] = True
    q = deque([(0, 0, 0)])
    best = int(1e19)
    while q:
        r, c, t = q.popleft()
        if r == N-1 and c == M-1:
            best = min(best, t)
            break
        if t == T:
            continue

        for mr, mc in move:
            nr, nc = r + mr, c + mc
            if not 0 <= nr < N or not 0 <= nc < M or visited[nr][nc]:
                continue

            if board[nr][nc] == 2:
                dist = t+1+(N-1-nr)+(M-1-nc)
                if dist <= T:
                    best = min(best, dist)
                visited[nr][nc] = True
            if board[nr][nc] == 0:
                q.append((nr, nc, t+1))
                visited[nr][nc] = True
    print(best if best < int(1e19) else "Fail")

main()