import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[-1] * N for _ in range(N)]
    if board[0][0] == 0:
        dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0: continue
            down, right = -1, -1
            if i > 0:
                down = dp[i-1][j]
                if (down+1) % 3 == board[i][j]:
                    down += 1
            if j > 0:
                right = dp[i][j-1]
                if (right+1) % 3 == board[i][j]:
                    right += 1
            dp[i][j] = max(down, right)
    print(dp[N-1][N-1]+1)
    
main()