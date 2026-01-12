import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    MOD = 1000000007
    S = int(input())
    N = len(input())

    dp = [0] * (S + 1)
    dp[0] = 1 

    for _ in range(N):
        nextdp = [0] * (S + 1)
        curSum = 0
        
        for j in range(S + 1):
            curSum = (curSum + dp[j]) % MOD
            if j >= 26:
                curSum = (curSum - dp[j - 26] + MOD) % MOD
            nextdp[j] = curSum
        dp = nextdp
    print(dp[S])

main()