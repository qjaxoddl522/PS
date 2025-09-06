import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    move = ((0, 1), (1, 0), (0, -1), (-1, 0))
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    q = deque()
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1:
                q.appendleft((r, c, 1))
            elif board[r][c] == 2:
                q.append((r, c, 2))
    
    while True:
        qNext = deque()
        # 현재 감염 중인 1번 바이러스의 위치
        one = set()
        while q:
            r, c, v = q.popleft()
            for mr, mc in move:
                nr, nc = r + mr, c + mc
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                if board[nr][nc] == 0:
                    if v == 2 and (nr, nc) in one:
                        board[nr][nc] = 3
                    elif v == 1:
                        one.add((nr, nc))
                    else:
                        board[nr][nc] = v
                        qNext.append((nr, nc, v))
        for r, c in one:
            if board[r][c] != 3:
                board[r][c] = 1
                qNext.appendleft((r, c, 1))
        if not qNext:
            break
        q = qNext
    
    ans = [0] * 3
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:
                ans[board[r][c]-1] += 1
    print(*ans)

main()