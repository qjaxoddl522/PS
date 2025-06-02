import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    MOD = 1000000007
    # i * 3 의 크기에 타일이 들어가는 경우의 수
    dp = [0] * (10000 // 3 + 1)
    dp[1] = 3
    n = 10000 // 3
    for i in range(2, n+1):
        # 기본 전이
        dp[i] = dp[i-1] * 3
        # 여러 타일에 걸침
        for j in range(2, i):
            dp[i] = (dp[i] + (dp[i-j] * j * 2)) % MOD
        # 중복이 없는 여러 타일에 걸침
        dp[i] = (dp[i] + (i * 2)) % MOD
    
    for _ in range(int(input())):
        N = int(input())
        print(dp[N//3] if N % 3 == 0 else 0)

main()