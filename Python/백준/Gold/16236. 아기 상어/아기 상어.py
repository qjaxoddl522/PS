import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N = int(input())
    board = []
    
    shark = None
    for r in range(N):
        temp = list(map(int, input().split()))
        for c in range(N):
            if temp[c] == 9:
                shark = (r, c, 0)
                temp[c] = 0
        board.append(temp)
    
    answer = 0
    sharkSize = 2
    need = sharkSize
    
    while True:
        # 가까운 물고기 찾기
        dq = deque([shark])
        visited = [[False] * N for _ in range(N)]
        visited[shark[0]][shark[1]] = True
        fishDist = 0
        nextShark = None
        
        while dq:
            r, c, move = dq.popleft()
            if 0 < fishDist < move:
                break
            
            if 0 < board[r][c] < sharkSize:
                if nextShark == None or r < nextShark[0] or (r == nextShark[0] and c < nextShark[1]):
                    nextShark = (r, c)
                fishDist = move
                continue
            
            for mr, mc in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                nr, nc = r + mr, c + mc
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] <= sharkSize and not visited[nr][nc]:
                    dq.append((nr, nc, move+1))
                    visited[nr][nc] = True
        
        if fishDist == 0:
            break
        
        answer += fishDist
        shark = (nextShark[0], nextShark[1], 0)
        board[nextShark[0]][nextShark[1]] = 0
        need -= 1
        if need == 0:
            sharkSize += 1
            need = sharkSize
    print(answer)
    
main()
