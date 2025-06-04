import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    move = ((1, 0), (-1, 0), (0, 1), (0, -1))
    R, C = map(int, input().split())
    board = []

    visited = [[False] * C for _ in range(R)]
    # 지훈
    q = deque()
    # 불
    fq = deque()

    for r in range(R):
        inp = list(input())
        for c in range(C):
            if inp[c] == 'J':
                inp[c] = '.'
                visited[r][c] = True
                q.append((r, c, 0))
            if inp[c] == 'F':
                fq.append((r, c, 0))
        board.append(inp)
    
    time = 0
    escaped = False
    while q and not escaped:

        # 현재 시간의 불 옮겨붙기
        while fq and time == fq[0][2]:
            r, c, t = fq.popleft()

            for mr, mc in move:
                nr, nc = r + mr, c + mc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == '.':
                    board[nr][nc] = 'F'
                    fq.append((nr, nc, t+1))
        
        # 현재 시간의 지훈이 이동
        while q and time == q[0][2]:
            r, c, t = q.popleft()

            if r == 0 or r == R-1 or c == 0 or c == C-1:
                escaped = True
                break

            for mr, mc in move:
                nr, nc = r + mr, c + mc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and board[nr][nc] == '.':
                    visited[nr][nc] = True
                    q.append((nr, nc, t+1))
        
        time += 1
    # 탈출하지 못한 채 큐가 종료되었으면 불가능
    print(time if escaped else "IMPOSSIBLE")

main()