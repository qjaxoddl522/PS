import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]

    ans = 2
    for j in range(1, N):
        up, down = board[0][j], board[1][j]
        prevUp, prevDown = board[0][j-1], board[1][j-1]
        if (up == 0 and prevDown == 0) or (down == 0 and prevUp == 0) or (up == 0 and down == 0):
            ans = 0
            break
        if up == 0 or down == 0:
            ans = 1
    print(ans)

main()