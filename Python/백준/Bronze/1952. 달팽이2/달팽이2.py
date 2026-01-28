import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    board = [[False] * M for _ in range(N)]

    x, y = 0, 0
    dir = 0
    rot = 0
    while (y+1 < N and not board[y+1][x]) or (x+1 < M and not board[y][x+1])\
        or (y-1 >= 0 and not board[y-1][x]) or (x-1 >= 0 and not board[y][x-1]):
        board[y][x] = True
        if dir == 0:
            x += 1
            if x + 1 == M or board[y][x+1]:
                dir = (dir + 1) % 4
                rot += 1
        elif dir == 1:
            y += 1
            if y + 1 == N or board[y+1][x]:
                dir = (dir + 1) % 4
                rot += 1
        elif dir == 2:
            x -= 1
            if x - 1 < 0 or board[y][x-1]:
                dir = (dir + 1) % 4
                rot += 1
        elif dir == 3:
            y -= 1
            if y - 1 < 0 or board[y-1][x]:
                dir = (dir + 1) % 4
                rot += 1
    print(rot - 1)
    
main()