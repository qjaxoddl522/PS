import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    MOD = 10_007
    N = int(input())

    # dp[i][j][k] = i번째 줄에서 왼쪽이 j번째 오른쪽이 k번째에 있을 때 가능한 경로 경우의 수
    dp = [[[0] * (i+1) for _ in range(i+1)] for i in range(N)]
    dp[0][0][0] = 1
    for i in range(1, N):
        for j in range(i):
            for k in range(j+1, i+1):
                if k < i:
                    dp[i][j][k] += dp[i-1][j][k]
                    if j > 0:
                        dp[i][j][k] += dp[i-1][j-1][k]
                if k > 0:
                    dp[i][j][k] += dp[i-1][j][k-1]
                if j > 0 and k > 0:
                    dp[i][j][k] += dp[i-1][j-1][k-1]
                dp[i][j][k] %= MOD
    ans = 0
    for j in range(N):
        ans = (ans + sum(dp[N-1][j])) % MOD
    print((ans*2) % MOD if N > 1 else ans)

main()