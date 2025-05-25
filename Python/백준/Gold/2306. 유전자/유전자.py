import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    inp = input()
    N = len(inp)

    # dp[i][j] = i부터 j까지의 최대 KOI유전자 길이
    dp = [[0] * N for _ in range(N)]
    for L in range(1, N):
        for i in range(N-L):
            if (inp[i] == 'a' and inp[i+L] == 't') or (inp[i] == 'g' and inp[i+L] == 'c'):
                dp[i][i+L] = max(dp[i][i+L], dp[i+1][i+L-1] + 2)
            # 감싸기
            dp[i][i+L] = max(dp[i][i+L], dp[i+1][i+L], dp[i][i+L-1])
            # 합치기
            for k in range(i, i+L):
                dp[i][i+L] = max(dp[i][i+L], dp[i][k] + dp[k+1][i+L])
    print(dp[0][N-1])

main()