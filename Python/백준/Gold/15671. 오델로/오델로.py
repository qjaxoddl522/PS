import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    dir = ((0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
    size = 6
    # 양수면 흑, 음수면 백 승리
    point = 0
    N = int(input())
    board = [['.' for _ in range(size)] for _ in range(size)]
    board[2][2] = board[3][3] = 'W'
    board[2][3] = board[3][2] = 'B'

    for i in range(N):
        R, C = map(int, input().split())
        R, C = R-1, C-1
        me = 'B' if i % 2 == 0 else 'W'
        board[R][C] = me
        point += 1 if i % 2 == 0 else -1
        for r, c in dir:
            posR, posC = R+r, C+c
            while True:
                if posR < 0 or posC < 0 or posR >= size or posC >= size or board[posR][posC] == '.':
                    break
                if board[posR][posC] == me:
                    rr, cc = R+r, C+c
                    while posR != rr or posC != cc:
                        board[rr][cc] = me
                        point += 2 if i % 2 == 0 else -2
                        rr, cc = rr+r, cc+c
                    break
                posR, posC = posR+r, posC+c

    for row in board:
        print(''.join(row))
    
    print("Black" if point > 0 else "White")

main()