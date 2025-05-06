import sys, math
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
    MAX = float('inf')
    
    W, H = map(int, input().split())
    board = [list(input()) for _ in range(H)]

    time = [[MAX] * W for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    # 전처리
    start = None
    for r in range(H):
        for c in range(W):
            if board[r][c] == 'T':
                start = (r, c)
                board[start[0]][start[1]] = 0
            elif board[r][c] == 'E':
                end = (r, c)
            elif board[r][c] != 'R' and board[r][c] != 'H':
                board[r][c] = int(board[r][c])
    
    # 다익스트라
    q = [(0, start[0], start[1])]
    while q:
        t, r, c = heappop(q)
        if visited[r][c]:
            if board[r][c] == 'E':
                break
            continue
        visited[r][c] = True
        
        for dr, dc in direction:
            mr, mc, mt = r, c, t
            while True:
                nr = mr + dr
                nc = mc + dc
                if not (0 <= nr < H and 0 <= nc < W):
                    break

                if board[nr][nc] == 'R':
                    if time[mr][mc] > mt:
                        heappush(q, (mt, mr, mc))
                        time[mr][mc] = mt
                    break
                if board[nr][nc] == 'H':
                    break
                if board[nr][nc] == 'E':
                    if time[nr][nc] > mt:
                        heappush(q, (mt, nr, nc))
                        time[nr][nc] = mt
                    break
                
                mr = nr
                mc = nc
                mt += board[mr][mc]
    
    result = time[end[0]][end[1]]
    print(result if result != MAX else -1)

main()