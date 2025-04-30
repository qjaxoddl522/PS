import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    MOD = 1000000007
    M = int(input())

    T = M * 6 - 21
    # dp[i] = 합이 21+i일 경우 경우의 수
    dp = [1] + [0] * T

    for side in range(1, 7):
        for n in range(side, T+1):
            dp[n] = (dp[n] + dp[n-side]) % MOD
    
    result = 0
    for n in range(T+1):
        result = (result + dp[n]) % MOD
    
    print((result * 30) % MOD)

main()