import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    H = int(input())

    dp = [[float('inf')] * M for _ in range(N)]
    dp[0][0] = board[0][0]
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                continue
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            dp[i][j] += board[i][j]
    res = dp[N-1][M-1]
    if res <= H:
        print("YES")
        print(res)
    else:
        print("NO")
    
main()