import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def Main():
    move = ((1, 0), (0, 1), (-1, 0), (0, -1))
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    vals = sorted({v for row in board for v in row})
    U = len(vals)
    # 최대 D의 차이로 통과 가능한지 확인
    def Check(D):
        s = board[0][0]
        t = board[N-1][N-1]

        hi = 0
        for lo in range(U):
            while hi < U and vals[hi] - vals[lo] <= D:
                hi += 1
            if hi - 1 < lo:
                continue
            low, high = vals[lo], vals[hi - 1]

            if not (low <= s <= high and low <= t <= high):
                continue
            
            q = deque([(0, 0)])
            visited = [bytearray(N) for _ in range(N)]
            visited[0][0] = 1

            while q:
                r, c = q.popleft()
                if r == N - 1 and c == N - 1:
                    return True
                for mr, mc in move:
                    nr, nc = r + mr, c + mc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        v = board[nr][nc]
                        if low <= v <= high:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
        return False
    
    minn, maxx = 200, 0
    for row in board:
        minn = min(minn, min(row))
        maxx = max(maxx, max(row))
    
    L, R = 0, maxx - minn
    while L <= R:
        mid = (L + R) // 2
        if Check(mid):
            R = mid - 1
        else:
            L = mid + 1
    print(L)

Main()