import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    prefix = 0
    dp = [0] * (N+1)
    for i in range(2, N+1):
        prefix += dp[i-2]
        # dp[i-1] => 오른쪽
        # prefix => 왼쪽으로 누적된 그룹 수
        dp[i] = dp[i-1] + prefix + (1 if i % 2 == 0 else 0)
    print(dp[N])

main()