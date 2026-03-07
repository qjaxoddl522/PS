import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    move = ((1, 0), (0, 1), (-1, 0), (0, -1))
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    HR, HC = map(int, input().split())
    HR -= 1; HC -= 1

    vision = [[False for _ in range(C)] for _ in range(R)]

    for cmd in input():
        # 와드 설치
        if cmd == 'W' and not vision[HR][HC]:
            area = board[HR][HC]
            vision[HR][HC] = True
            q = deque([(HR, HC)])
            while q:
                r, c = q.popleft()
                for mr, mc in move:
                    nr, nc = r + mr, c + mc
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == area and not vision[nr][nc]:
                        vision[nr][nc] = True
                        q.append((nr, nc))
        elif cmd == 'U':
            HR -= 1
        elif cmd == 'D':
            HR += 1
        elif cmd == 'L':
            HC -= 1
        elif cmd == 'R':
            HC += 1
    
    # 도착한 위치 밝히기
    for nr in range(HR-1, HR+2):
        if 0 <= nr < R:
            vision[nr][HC] = True
    for nc in range(HC-1, HC+2):
        if 0 <= nc < C:
            vision[HR][nc] = True
    
    # 출력
    for r in range(R):
        for c in range(C):
            print('.' if vision[r][c] else '#', end='')
        print()
    
main()